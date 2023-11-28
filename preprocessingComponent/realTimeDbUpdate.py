from .retrieveRawTables import retrieveTables
from .models import UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw

from .preprocessTables import preprocessTables

from MLComponent import ml_models

tableNames = ["course-info","course-rating", "tag", "user-list"]
modelNames = [UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw]

# retrieve tables
def retrieveAllRawTables(): 
    # Raw
    # course_info raw
    for modelName in modelNames: 
        if len(modelName.objects.all()): 
            modelName.objects.all().delete()

    for tableName in tableNames: 
        ttlPages = 0
        currPageNum = 1
        status = False
        while (ttlPages != currPageNum): 
            status, ttlPages, currPageNum = retrieveTables(tableName, currPageNum, currPageNum+9)
            if type(status) == bool: 
                print("LOOP ITERATION CHANGED", status, ttlPages, currPageNum, tableName)
            else: 
                return status
    if status: 
        return {"status": "whole database updated with new data"}
    # # tags raw
    # retrieveTables("tags")
    # # course_ratings raw
    # retrieveTables("course-ratings")
    # # user_list raw
    # retrieveTables("user-list")

def preprocessAllRawTables(): 
    # Preprocess
    # course_info preprocessed
    status_courseInfo = preprocessTables("course-info")
    # tags preprocessed
    # course_ratings preprocessed
    status_courseRatings = preprocessTables("course-rating")
    # user_list preprocessed
    status_userList = preprocessTables("user-list")
    return {"status_courseInfo ": status_courseInfo,"status_courseRatings": status_courseRatings, "status_userList": status_userList}
    

def modelForAllAlgorithms(): 
    # modeling
    # SVD
    trainset, testset = ml_models.trainset_and_testset_rating()
    status_svd = ml_models.train_and_test_svdModel(trainset, testset, "rating")

    # NCF
    status_ncf = ml_models.buildModelForNCF()

    return {"status_svd": status_svd, "status_ncf": status_ncf}
# content_based
# cosine_sim 
# predictions_rating_df

# SVD

# NCF
