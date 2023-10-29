import numpy as np
import pandas as pd
from courseRecoSystem.imports import dataImports



def mapIdsToAnotherDf(idList: list, referenceDf: pd.DataFrame):
    res = []
    if not pd.isna([idList]).any():
        for i in idList:
            res.extend(referenceDf[referenceDf['id']==i]["tag_name"])
        return res
    else:
        return ''

def applyLowerCase(val: str) -> str:
    if isinstance(val, str):
        return str.lower(val)
    else:
        return ''

def applyDictKeysLowerCase(in_dict):
    if type(in_dict) is dict:
        out_dict = {}
        for key, item in in_dict.items():
            out_dict[key.lower()] = applyDictKeysLowerCase(item)
        return out_dict
    elif type(in_dict) is list:
        return [applyDictKeysLowerCase(obj) for obj in in_dict]
    else:
        return in_dict

def checkCourseInDb(course_id: int):
    if not (dataImports.data_course_list['id'].isin([course_id]).any()): 
        return False, {"status": f"Error: course with course_id {course_id} does not exist in the database."}
    else: 
        return True, {}

def checkUserInDb(user_id: int):
    if not (dataImports.data_user_list['id'].isin([user_id]).any()): 
        return False, {"status": f"Error: user with user_id {user_id} does not exist in the database. Use content based recommendation with course id. eg.: `api/get_recommendation/content_based/<course_id>`"}
    else: 
        return True, {}
