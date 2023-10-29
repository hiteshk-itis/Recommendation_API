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

def checkCourseInDb(course_id: int):
    if not (dataImports.data_course_list['id'].isin([course_id])): 
        return False, {"status": f"Error: course with {course_id} does not exist in the datbase."}
    else: 
        return True, {}

def checkUserInDb(user_id: int):
    if not (dataImports.data_user_list['id'].isin([user_id])): 
        return False, {"status": f"Error: user with {user_id} does not exist in the datbase."}
    else: 
        return True, {}
