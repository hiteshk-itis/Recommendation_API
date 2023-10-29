from .retrieveRawTables import retrieveTables

# retrieve tables
def retrieveAllRawTables(): 
    # Raw
    # course_info raw
    retrieveTables("course_info")
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
