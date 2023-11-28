from .models import CourseInfoRaw, TagsRaw, UserListRaw, CourseRatingRaw, CourseInfoPreprocessed, TagsPreprocessed, UserListPreprocessed, CourseRatingPreprocessed

from datetime import datetime
from courseRecoSystem import utilsFunctions
import numpy as np
import pandas as pd
import neattext.functions as nfx

# classes: making pipelines
## preprocessing CourseList Pipeline
class PreprocessingCourseList:

  def __init__(self, _df: pd.DataFrame):
    self.df = _df.copy()
    self.df.name = "course_list"
    self.colToChange = "tag"
    self.resultCols = ["id", "course_name", "tag", "center_code"]
    self.df = self.df.dropna(subset=['center_code'])

  def makeColNamesLowerCase(self) -> list:
    self.df.columns = [str.lower(str(val)) for val in self.df.columns]
    return self.df.columns

  # converting the tag column into array of integers
  def convertToListOfIntegers(self) -> pd.Series:
    self.df[self.colToChange] = self.df[self.colToChange].apply(lambda val: np.array(val.split(',')).astype(int) if (not pd.isna(val)) else np.nan)
    return self.df[self.colToChange]

  def truncateDf(self) -> pd.DataFrame:
    self.df.drop([x for x in self.df.columns[~self.df.columns.isin(self.resultCols)]], axis = 1, inplace = True)
    return self.df


  def changeTagColToTagNames(self, referenceDf: pd.DataFrame):
    self.df[self.colToChange] = self.df[self.colToChange].apply(lambda val: utilsFunctions.mapIdsToAnotherDf(val, referenceDf))

  def joinValsInList(self):
    for i in range(len(self.df[self.colToChange])):
      if i == 97: 
        self.df[self.colToChange][i]=''
        continue
      val = self.df[self.colToChange][i]
      val1 = type(self.df[self.colToChange][i])
      val2 = self.df[self.colToChange]
      l = len(self.df[self.colToChange])
      if self.df[self.colToChange][i]!=[]:
          self.df[self.colToChange][i]=' '.join(self.df[self.colToChange][i])
      else:
          self.df[self.colToChange][i]=' '.join(self.df[self.colToChange][i])
    return self.df[self.colToChange]

  def convertTagColumnToLowerCase(self):
    self.df[self.colToChange] = self.df[self.colToChange].apply(utilsFunctions.applyLowerCase)

  def makeNLPChanges(self):
    self.df[self.colToChange]=self.df[self.colToChange].apply(nfx.remove_stopwords)
    self.df[self.colToChange]=self.df[self.colToChange].apply(nfx.remove_special_characters)
    self.df[self.colToChange]=self.df[self.colToChange].apply(nfx.remove_puncts)
    self.df[self.colToChange]=self.df[self.colToChange].apply(nfx.remove_numbers)

  def getDf(self) -> pd.DataFrame:
    return self.df

from nltk.stem import PorterStemmer
from googletrans import Translator
import re
import numpy as np
from numba import jit, cuda

## preprocessing Tags Pipeline
class PreprocessingTags: 
  def __init__(self, _df: pd.DataFrame): 
    self.df = _df.copy()
    self.df.name = "tags"
    self.initialTags = self.df["tag_name"]
    self.resultTags = []
    self.resultCols = ["id", "tag_name"]
    

  def makeColNamesLowerCase(self) -> list:
    self.df.columns = [str.lower(str(val)) for val in self.df.columns]
    return self.df.columns

  def makeValsLowerCase(self): 
    self.resultTags = self.initialTags.apply(str.lower)

  def removeUsingRegex(self): 
    tag = []
    for word in self.resultTags:
      # tag.append(process_tag(word))
      tag.append(re.sub(r'https?:\/\/.*[\r\n]*','.',word))    
    self.resultTags = np.array(tag)
    return self.resultTags

  @jit(target_backend='cuda')
  def translateTags(self) -> list:
    tags = np.array([])
    untranslatedTags = self.resultTags
    for word in np.array(untranslatedTags):
      translator = Translator()
      translated_tag_names = translator.translate(word, src='id', dest='en').text
      np.append(tags, translated_tag_names)
    self.resultTags = tags
    return self.resultTags

  def truncateDf(self) -> pd.DataFrame:
    self.df.drop([x for x in self.df.columns[~self.df.columns.isin(self.resultCols)]], axis = 1, inplace = True)
    return self.df

  def takeStemVals(self): 
    stemmer = PorterStemmer()
    tags_stem = []
    # tags_list = self.df["tag_name"].to_list()
    for word in self.resultTags: 
      stem_word = stemmer.stem(word)
      tags_stem.append(stem_word)
    self.resultTags = np.array(tags_stem)
    return tags_stem

  def updateTagsColumnInTable(self): 
    self.df["tag_name"] = self.resultTags
    return self.df

  def getDf(self): 
    return self.df
   

# Functions: Making use of pipelines

def preprocessTags(): 
  try: 
    tagsTableObj
  except: 
    varExists = False
  else: 
    varExists = True

  if varExists: 
    del tagsTableObj

  tagsRaw = pd.DataFrame.from_records(TagsRaw.objects.all().values())
  tagsTableObj = PreprocessingTags(tagsRaw)
  tagsTableObj.makeColNamesLowerCase()
  tagsTableObj.makeValsLowerCase()
  tagsTableObj.removeUsingRegex()
  tagsTableObj.translateTags()
  tagsTableObj.truncateDf()
  tagsTableObj.takeStemVals()
  tagsTableObj.updateTagsColumnInTable()
  return tagsTableObj.getDf()

def preprocessCourseInfo(): 
  try: 
    courseListObj
  except: 
    varExists = False
  else: 
    varExists = True

  if varExists: 
    del courseListObj

  courseInfoRawDf = pd.DataFrame.from_records(CourseInfoRaw.objects.all().values())
  preprocessedTags = pd.DataFrame.from_records(TagsPreprocessed.objects.all().values())

  courseListObj = PreprocessingCourseList(courseInfoRawDf)
  courseListObj.makeColNamesLowerCase()
  # courseListObj.convertToListOfIntegers()
  courseListObj.truncateDf()
  courseListObj.changeTagColToTagNames(preprocessedTags)
  finalTable3 = courseListObj.getDf()
  courseListObj.joinValsInList()
  finalTable4 = courseListObj.getDf()
  courseListObj.convertTagColumnToLowerCase()
  courseListObj.makeNLPChanges()
  finalTable = courseListObj.getDf()
  print("##################",courseListObj.getDf().iloc[0, :])
  return courseListObj.getDf()
  
def preprocessUserList(): 
  user_list = pd.DataFrame.from_records(UserListRaw.objects.all().values())

  # user_list["register_datetime"] = user_list["register_datetime"].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))

  # user_list["updated_datetime"] = user_list["updated_datetime"].apply(lambda x: datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))
  return user_list

def preprocessCourseRatings(): 

  course_rating = pd.DataFrame.from_records(CourseRatingRaw.objects.all().values())
  dfGrpByStdCourse = course_rating.groupby(['student', 'course_code'])
  dfGrpByStdCourseCount = pd.DataFrame(dfGrpByStdCourse.count())
  dfGrpByStdCourseMean = pd.DataFrame(dfGrpByStdCourse.mean())
  dfGrpByStdCourseMean.sort_values('rating', ascending=False)
  stdCourseMap = pd.DataFrame(dfGrpByStdCourseMean['rating']).reset_index()
  return stdCourseMap  
  
# The main function to be called
def preprocessTables(tableName: str):   
  tableNameModelMap = {
    "course-info": CourseInfoPreprocessed, 
    "course-rating": CourseRatingPreprocessed, 
    "tag": TagsPreprocessed, 
    "user-list": UserListPreprocessed, 
  }

  if len(tableNameModelMap[tableName].objects.all()):
    tableNameModelMap[tableName].objects.all().delete()


  if tableName == "tags": 
    df = preprocessTags()
    # df = pd.read_pickle("oct19_2023/tag_preprocessed.pkl")
    model_df = TagsPreprocessed

    model_instances = [
            model_df(
                id = tags_raw_record["id"], 
                tag_name = tags_raw_record["tag_name"], 
            ) for tags_raw_record in df.to_dict('records')
        ]

  elif tableName == "course-info": 
    df = preprocessCourseInfo()
    model_df = CourseInfoPreprocessed

    model_instances = [
        model_df(
            id = courseInfo_raw_record["id"]  ,
            course_name = courseInfo_raw_record["course_name"],
            center_code = courseInfo_raw_record["center_code"],
            tag = courseInfo_raw_record["tag"]
        )
            for courseInfo_raw_record in df.to_dict('records')
        ]
  elif tableName == "user-list": 
    df = preprocessUserList()
    model_df = UserListPreprocessed
    model_instances = [
            model_df(
                id = userList_raw_record["id"],
                username = userList_raw_record["username"],
                first_name = userList_raw_record["first_name"],
                last_name = userList_raw_record["last_name"],
                email = userList_raw_record["email"],
                is_active = userList_raw_record["is_active"],
                member_id = userList_raw_record["member_id"],
                member_permanent_address = userList_raw_record["member_permanent_address"],
                member_temporary_address = userList_raw_record["member_temporary_address"],
                member_birthdate = userList_raw_record["member_birthdate"],
                member_phone = userList_raw_record["member_phone"],
                use_flag = userList_raw_record["use_flag"],
                register_datetime = userList_raw_record["register_datetime"],
                register_agent = userList_raw_record["register_agent"],
                updated_datetime = userList_raw_record["updated_datetime"],
                is_teacher = userList_raw_record["is_teacher"],
                is_student = userList_raw_record["is_student"],
                is_center_admin = userList_raw_record["is_center_admin"],
                member_memo = userList_raw_record["member_memo"],
                member_avatar = userList_raw_record["member_avatar"],
                member_department = userList_raw_record["member_department"],
                member_position = userList_raw_record["member_position"],
                center_code = userList_raw_record["center_code"]
            ) for userList_raw_record in df.to_dict('records')
        ]
  elif tableName == "course-rating":
    df = preprocessCourseRatings()
    model_df = CourseRatingPreprocessed
    model_instances = [
            model_df(
                student = courseRatings_raw_record["student"],
                course_code = courseRatings_raw_record["course_code"],
                rating = courseRatings_raw_record["rating"]
            ) for courseRatings_raw_record in df.to_dict('records')
        ]
  else: 
    return {"status": f"invalid table name {tableName}"}

  if len(model_df.objects.all()): 
        model_df.objects.all().delete()

  model_df.objects.bulk_create(model_instances)
  
  return {"status": f"preprocessed {tableName} data updated"}
  