import requests
import pandas as pd
import numpy as np
import os
from dotenv import load_dotenv

load_dotenv()
from courseRecoSystem.utilsFunctions import applyDictKeysLowerCase
from .models import UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw
from courseRecoSystem import utilsFunctions

KOREAN_URL = os.getenv('KOREAN_URL')
KOREAN_TOKEN = os.getenv('KOREAN_TOKEN')
INDONESIAN_URL = os.getenv('INDONESIAN_URL')
INDONESIAN_TOKEN = os.getenv('INDONESIAN_TOKEN')
RECO_URL = os.getenv('RECO_URL')
RECO_TOKEN = os.getenv('RECO_TOKEN')

def getDataFrameFromAPI(tableName:str = "", serverName:str = "indonesian", startPage: int = 1, numData: int | str = 20, uptoPage: int = None) -> pd.DataFrame | dict:
  if serverName == "indonesian":
    url = INDONESIAN_URL
    token = INDONESIAN_TOKEN
  elif serverName == "korean":
    url = KOREAN_URL
    token = KOREAN_TOKEN
  else:
    raise Exception("serverName Error: either `indonesian` or `korean`")

  tableNameFunctionMap = {
    "course-info": saveIntoCourseInfo, 
    "course-rating": saveIntoCourseRatings, 
    "tag": saveIntoTags, 
    "user-list": saveIntoUserList, 
  }

  result = []
  if numData == "all":
    pageNum = startPage
    numData = 30
    total_pages = 0

    while True:
      r = requests.get(url + tableName,
                params = {
                    "page": pageNum,
                    "size": numData
                },
                headers = {
                    "Authorization": "token "+ token
                })
      resp = r.json()
      total_pages = resp["total_pages"]
      print(f"reading page: {pageNum}/{total_pages}")
      if "results" in list(resp.keys()):
        result.extend(resp["results"])

      if (resp["has_next"]):
        pageNum += 1
        continue
      else:
        break
    return pd.DataFrame(result)
  
  elif uptoPage is not None: 
    total_pages = 0
    pageNum = startPage
    while (pageNum != uptoPage+1): 
      result = []
      r = requests.get(url + tableName,
              params = {
                  "page": pageNum,
                  "size": numData
              },
              headers = {
                  "Authorization": "token "+ token
              })
      resp = r.json()
      total_pages = resp["total_pages"]
      
      print(f"reading page: {pageNum}/{total_pages}")
      if "results" in list(resp.keys()):
        result.extend(resp["results"])
        tableNameFunctionMap[tableName](utilsFunctions.applyDictKeysLowerCase(result))

      if (resp["has_next"]):
        pageNum += 1
      else: 
        break
    return True, total_pages, pageNum

  else:
    pageNum = startPage
    nData = numData
    while True:
      r = requests.get(url + tableName,
                params = {
                    "page": pageNum,
                    "size": nData
                },
                headers = {
                    "Authorization": "token "+ token
                })
      if not r.status_code == 404:
        data = r.json()
        if "results" in list(data.keys()):
          result.extend(data["results"])

          if (len(result) < numData):
            pageNum += 1
            nData = numData - len(result)
            continue
          else:
            return pd.DataFrame(result)

        else:
          return data

def makeColNamesLowerCase(df:pd.DataFrame) -> list:
  df.columns = [str.lower(str(val)) for val in df.columns]
  return df

def retrieveTables(tableName: str, currPageNum = 1, _uptoPage = 40): 
    url = INDONESIAN_URL
    token = INDONESIAN_TOKEN
    pageNum = currPageNum
    numData = 30
    total_pages = 0
    uptoPage = _uptoPage

    if not (tableName in ["course-info", "course-rating", "tag", "user-list"]): 
      return {"status": f"Error: table name {tableName} specified does not exist."}, 0, 0

    status, total_pages, pageNum = getDataFrameFromAPI(tableName, startPage = currPageNum, numData = 30, uptoPage = _uptoPage)
    return status, total_pages, pageNum

def saveIntoCourseInfo(courseInfo_raw): 
  model_df = CourseInfoRaw
  model_instances = [
        model_df(
            id = courseInfo_raw_record["id"]  ,
            course_name = courseInfo_raw_record["course_name"],
            course_code = courseInfo_raw_record["course_code"],
            course_description = courseInfo_raw_record["course_description"],
            course_cover_file = courseInfo_raw_record["course_cover_file"],
            course_level = courseInfo_raw_record["course_level"],
            course_info = courseInfo_raw_record["course_info"],
            use_flag = courseInfo_raw_record["use_flag"],
            register_datetime = courseInfo_raw_record["register_datetime"],
            updated_datetime = courseInfo_raw_record["updated_datetime"],
            register_agent = courseInfo_raw_record["register_agent"],
            course_provider = courseInfo_raw_record["course_provider"],
            syllabus = courseInfo_raw_record["syllabus"],
            keyword = courseInfo_raw_record["keyword"],
            center_code = courseInfo_raw_record["center_code"],
            tag = courseInfo_raw_record["tag"],
        )
            for courseInfo_raw_record in courseInfo_raw
        ]
  model_df.objects.bulk_create(model_instances)
  print("Database Updated")
  del model_instances
  return True

def saveIntoUserList(userList_raw): 
  model_df = UserListRaw
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
                is_center_admin = userList_raw_record["is_centeradmin"],
                member_memo = userList_raw_record["member_memo"],
                member_avatar = userList_raw_record["member_avatar"],
                member_department = userList_raw_record["member_department"],
                member_position = userList_raw_record["member_position"],
                center_code = userList_raw_record["center_code"]
            ) for userList_raw_record in userList_raw
        ]
  model_df.objects.bulk_create(model_instances)
  print("Database Updated")
  del model_instances
  return True

def saveIntoCourseRatings(courseRatings_raw): 
  model_df = CourseRatingRaw
  model_instances = [
            model_df(
                rating_id = courseRatings_raw_record["rating_id"],
                rating = courseRatings_raw_record["rating"],
                chapter_code = courseRatings_raw_record["chapter_code"],
                student = courseRatings_raw_record["student"],
                course_code = courseRatings_raw_record["course_code"],
                center_code = courseRatings_raw_record["center_code"],
            ) for courseRatings_raw_record in courseRatings_raw
        ]
  model_df.objects.bulk_create(model_instances)
  print("Database Updated")
  del model_instances
  return True

def saveIntoTags(tags_raw): 
  model_df = TagsRaw
  model_instances = [
            model_df(
                id = tags_raw_record["id"], 
                tag_name = tags_raw_record["tag_name"], 
                created_at = tags_raw_record["created_at"], 
                updated_at = tags_raw_record["updated_at"]
            ) for tags_raw_record in tags_raw
        ]
  model_df.objects.bulk_create(model_instances)
  print("Database Updated")
  del model_instances
  return True