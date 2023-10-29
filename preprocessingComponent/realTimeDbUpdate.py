from .retrieveRawTables import retrieveTables
from .models import UserListRaw, CourseInfoRaw, CourseRatingRaw, TagsRaw
# retrieve tables
def retrieveAllRawTables(): 
    ttlPages = 0
    currPageNum = 158
    status = False
    # Raw
    # course_info raw
    if len(CourseInfoRaw.objects.all()): 
        CourseInfoRaw.objects.all().delete()

    while (ttlPages != currPageNum): 
        status, ttlPages, currPageNum = retrieveTables("course_info", currPageNum, currPageNum+9)
        print("LOOP ITERATION CHANGED", status, ttlPages, currPageNum)
    if status: 
        return {"status": "whole database updated with new data"}
    # tags raw
    retrieveTables("tags")
    # course_ratings raw
    retrieveTables("course_ratings")
    # user_list raw
    retrieveTables("user_list")
    pass

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
