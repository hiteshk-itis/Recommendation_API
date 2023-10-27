from preprocessingComponent.models import CourseInfoRaw, TagsRaw, UserListRaw, CourseRatingRaw, CourseInfoPreprocessed, TagsPreprocessed, UserListPreprocessed, CourseRatingPreprocessed

from .models import PredictionsRatingDf

from courseRecoOne.models import CourseList, UserList

import pickle as pkl
import pandas as pd
import json
from dotenv import load_dotenv
import os
import numpy as np
from courseRecoOne.views import CourseListViewSet
from courseRecoOne.serializers import CourseListSerializer
import tensorflow as tf
tf.compat.v1.reset_default_graph()

load_dotenv()

# Utils Function 
# def makeColNamesLowerCase(df:pd.DataFrame) -> list:
#   df.columns = [str.lower(str(val)) for val in df.columns]
#   return df.columns

# def rating_pipeline(course_rating: pd.DataFrame) -> pd.DataFrame:
#   dfGrpByStdCourse = course_rating.groupby(['student', 'Course_Code'])
#   dfGrpByStdCourseCount = pd.DataFrame(dfGrpByStdCourse.count())
#   dfGrpByStdCourseMean = pd.DataFrame(dfGrpByStdCourse.mean())
#   dfGrpByStdCourseMean.sort_values('rating', ascending=False)
#   stdCourseMap = pd.DataFrame(dfGrpByStdCourseMean['rating']).reset_index()
#   return stdCourseMap

# Data Imports and Reads
# data_df = pd.DataFrame.from_records(df.objects.all().values())
# data_df = pd.read_pickle("oct19_2023/preprocessedCourseInfoDf_oct19.pkl")
data_df = pd.DataFrame.from_records(CourseInfoPreprocessed.objects.all().values())

data_course_list = data_df
# data_course_list = pd.DataFrame.from_records(CourseList.objects.all().values())

# data_user_list = pd.read_pickle("oct19_2023/userList_Oct19.pkl")
data_user_list = pd.DataFrame.from_records(UserListPreprocessed.objects.all().values())

# def makeColNamesLowerCase(df:pd.DataFrame) -> list:
#   df.columns = [str.lower(str(val)) for val in df.columns]
#   return df.columns
# makeColNamesLowerCase(data_user_list)
# data_user_list = pd.DataFrame.from_records(UserList.objects.all().values())

# rating_Oct19 = pd.read_pickle('oct19_2023/rating_Oct19.pkl')
# rating = rating_pipeline(rating_Oct19)
rating = pd.DataFrame.from_records(CourseRatingPreprocessed.objects.all().values())

# indices=np.load("models/content_based/indices.pkl", allow_pickle=True)
indices=pd.Series(range(0, data_course_list['course_name'].size),index = data_course_list['course_name'].tolist())

indicesPkl = indices
# indicesPkl = pd.read_pickle('indices_content_based.pkl')

# cosine_sim = np.load('oct19_2023/cosineSim_Oct19.pkl', allow_pickle=True)
cosine_sim = np.load('models/content_based/cosineSim.pkl', allow_pickle=True)
# cosine_sim = pkl.load(open('MLComponent/cosine_sim.pkl', 'rb'))



def content_based(course_id, data=data_df, indices=indices, cosine_sim=cosine_sim):
    id=indices[course_id]
    sim=[(index, cosine_sim[id][index]) for index in range(len(cosine_sim[id]))]
    sim=sorted(sim,key=lambda x:x[1],reverse=True)
    sim=sim[1:15]
    index=[i[0] for i in sim]
    recommended_lst = list(data['course_name'].iloc[index])
    
    recommended_lst_dict_temp = []
    for x in recommended_lst:
        recommended_lst_dict_temp.append(data[data["course_name"]== x].to_dict('records'))
    
    recommended_lst_dict = []
    for i in range(0, len(recommended_lst_dict_temp)):
        recommended_lst_dict.append(recommended_lst_dict_temp[i][0])     
    
    return recommended_lst_dict

# Basis of Rating
def embed_user_information(userid, embed_for="rating"):
  # preparing resultant dictionary res_dict
  # get the name of the user from userid
  res_dict = data_user_list.loc[data_user_list['id'] == userid, ['id', 'username', 'email','center_code']].to_dict(orient="records")[0]

    # adding other keys in resultant dictionary
  res_dict['user_url'] = os.path.join(os.getenv('BASE_URL'), 'user_list', str(userid))

  if (embed_for == "rating"):
    # rated_courses
    rated_courses_id = rating.loc[rating['student'] == userid, ['course_code', 'rating']].values.tolist()
    rated_courses = []
    for i in rated_courses_id:
      rated_course_dict = data_course_list.loc[data_course_list['id'] == i[0], ['id', 'course_name', 'center_code']].to_dict('records')[0]
      rated_course_dict['rated'] = round(i[1], 2)
      rated_course_dict['course_url'] = os.path.join(os.getenv('BASE_URL'), 'course_list', str(int(i[0])))
      rated_courses.append(rated_course_dict)

    # resultant dictionary
    res_dict['rated_courses'] = rated_courses
    
  return res_dict

# def embed_user_information(userid): 
#   # resultant dictionary => res_dict
#   # get the name of the user from userid
#   res_dict = data_user_list.loc[data_user_list['id'] == userid, ['id', 'username', 'email', 'center_code']].to_dict(orient="records")[0]

#   # adding other keys in resultant dictionary
#   res_dict['user_url'] = os.path.join(os.getenv('BASE_URL'), 'user_list', str(userid))
  
#   # rated_courses
#   rated_courses_id = rating.loc[rating['student'] == userid, ['Course_Code', 'rating']].values.tolist()
#   rated_courses = []
#   for i in rated_courses_id:
#     rated_course_dict = data_course_list.loc[data_course_list['id'] == i[0], ['id', 'course_name']].to_dict('records')[0]
#     rated_course_dict['rated'] = round(i[1], 2)
#     rated_course_dict['course_url'] = os.path.join(os.getenv('BASE_URL'), 'course_list', str(int(i[0])))
#     rated_courses.append(rated_course_dict)
  
#   res_dict['rated_courses'] = rated_courses
#   return res_dict



def SVD_rating(userid, get_recommend =5):

  if (not data_user_list['id'].isin([userid]).any()): 
    return {"error": "provided userid does not exist"}

  res_dict = embed_user_information(userid)
  res_dict['recommended_courses'] = []

  predictions_df = pd.DataFrame.from_records(PredictionsRatingDf.objects.all().values())
  predictions_userID = predictions_df[predictions_df['uid'] == userid].sort_values(by="est", ascending = False).head(5) 
  
  if (predictions_userID.empty): 
    return res_dict

  # Series with index as the course_id and values as est rating
  iid_est_map = pd.Series(predictions_userID['est'].values.tolist(), index = predictions_userID['iid'].values.tolist())

  recommendations_id = []
  recommendations_id.append(list(predictions_userID['iid']))
  recommendations_id=recommendations_id[0]
  recommendations_subject = []
  recommended_courses = []
  
  
  # recommended course
  for i in recommendations_id:
    course_id_filter = data_course_list['id'].isin([i])
    center_code_filter = data_course_list['center_code'].isin([res_dict['center_code']])

    # checking whether the course has same center_code
    if(not (course_id_filter & center_code_filter).any()):
      break

    
    reco_course_dict = data_course_list.loc[course_id_filter & center_code_filter, ['id', 'course_name', 'center_code']].to_dict('records')[0]
    reco_course_dict['estimated_rating'] = round(iid_est_map[i], 2)
    reco_course_dict['course_url'] = os.path.join(os.getenv('BASE_URL'), 'course_list', str(i))
    recommended_courses.append(reco_course_dict)

    subjects = data_course_list.loc[data_course_list["id"] == i, "course_name"].tolist()
    recommendations_subject.extend(subjects)
    
  res_dict['recommended_courses'] = recommended_courses
  
  return res_dict

def overall_SVD_rating(num): 
  res = []
  for i in np.unique(rating['student'].tolist())[1:num+1]: 
    res.append(SVD_rating(i))

  return res


# basis of Quiz

# def SVD_quiz(userid, get_recommend=5):
#   model=SVD(n_factors=50,n_epochs=20,lr_all=0.005,reg_all=0.2)
#   model.fit(trainset)
#   testset = trainset.build_anti_testset()
#   prediction = model.test(testset)
#   prediction_df = pd.DataFrame(prediction)
#   prediction_userID = prediction_df[prediction_df['uid']==userid].sort_values(by="est",ascending=False).head(get_recommend)
#   recommendation = []
#   recommendation.append(list(prediction_userID["iid"]))
#   recommendation = recommendation[0]
#   recommendations_subject = []
#   for i in recommendation:
#     subjects = data_course_list.loc[data_course_list["id"] == i, "course_name"].tolist()
#     recommendations_subject.extend(subjects)
#   return recommendations_subject




# # # basis of Assignment




# API Implementation of NCF 

def content_based_ncf(course_name: str, data):
  id  = indices[course_name]# Obtain the index of the course that matches the title
  sim = [(index, cosine_sim[id][index]) for index in range(len(cosine_sim[id]))]#Get the pairwsie similarity scores of all course with that movie
  sim = sorted([item for item in sim if item[1] > 0.2],key=lambda x:x[1],reverse=True)# Sort the course based on the cosine similarity scores > 0.2
  sim = sim[1:]#Ignore the first course

  index=[i[0] for i in sim]#Get course index
  sim_score = [i[1] for i in sim]#Get course cosine similarity
  sim_score = [round(i,2)for i in sim_score]
  sim_score = [str(i) +' '+'(Similarity_Score)'for i in sim_score]
  course = list(data['Course_Name'].iloc[index])#return list of similar courses
  return (course, sim_score)

# For NCF
from libreco.data import random_split, DatasetPure, DataInfo
from libreco.algorithms import NCF
from libreco.evaluation import evaluate

# rating_cpy = rating.copy()

# rating_cpy.columns = ['user','item','label']

load_data_info = DataInfo.load('data_info_rating',model_name='ncfModelRating')

model1 = NCF.load('model_rating',model_name='ncfModelRating',data_info = load_data_info)


def NCF_rating_api(
    user_id,
    # course_name,
    number_recommendation = 5,
    data=data_course_list,
    indices=indicesPkl,
    cosine_sim=cosine_sim,
    user_list=data_user_list
    ):

  # embed user information
  res_dict = embed_user_information(user_id)

  #For Content Based part
  # course, sim_score = content_based_ncf(course_name, data = course_list)

  ##For Neural_Collaborative_Filtering_Part
  recommendation = model1.recommend_user(user = user_id,n_rec = number_recommendation )#returns recommended course_id for user

  # Formatting as json
  recommendations_id = recommendation[user_id]
  recommendations_subject = []
  recommended_courses = []
  for i in recommendations_id:
    course_id_filter = data_course_list['id'].isin([i])
    center_code_filter = data_course_list['center_code'].isin([res_dict['center_code']])

    if(not (course_id_filter & center_code_filter).any()):
      break
    reco_course_dict = data_course_list.loc[course_id_filter & center_code_filter, ['id', 'course_name','center_code']].to_dict('records')[0]
    # reco_course_dict['estimated_rating'] = round(iid_est_map[i], 2)
    reco_course_dict['estimated_rating'] =  float(model1.predict(user = user_id,item = i)[0])
    recommended_courses.append(reco_course_dict)

    subjects = data_course_list.loc[data_course_list["id"] == i, "course_name"].tolist()
    recommendations_subject.extend(subjects)

  res_dict['recommended_courses'] = recommended_courses
  
  return res_dict