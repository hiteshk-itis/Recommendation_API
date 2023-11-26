from .retrieveRawTables import retrieveTables
from .models import UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw
# retrieve tables
def retrieveAllRawTables(): 
    tableNames = ["course-info","course-rating", "tag", "user-list"]
    modelNames = [UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw]
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
    # tags preprocessed
    # course_ratings preprocessed
    # user_list preprocessed
    pass

def modelForAllAlgorithms(): 
    # modeling
    pass

# content_based
# cosine_sim 
# predictions_rating_df

# SVD

# NCF
