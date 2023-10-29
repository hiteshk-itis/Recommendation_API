# import pandas as pd
# import numpy as np
# import pickle

# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
# import sklearn
# from numba import jit, cuda

# @jit(target_backend = 'cuda')
# def makeCosineSimilarityMatrix(_df: pd.DataFrame, based_on_col: str) -> np.ndarray:
#   count: sklearn.feature_extraction.text.TfidfVectorizer =TfidfVectorizer()
#   count_matrix = count.fit_transform(_df[based_on_col])
#   cosine_sim = cosine_similarity(count_matrix,count_matrix)
#   return cosine_sim


# finalCourseList = pd.read_pickle("oct19_2023/preprocessedCourseInfoDf_oct19.pkl")
# cosineSim_Oct19 = makeCosineSimilarityMatrix(finalCourseList, "tag")

# f = open("oct19_2023/cosineSim_Oct19.pkl", "wb")
# pickle.dump(cosineSim_Oct19, f)
# f.close()


import requests
from dotenv import load_dotenv

load_dotenv()
RECO_URL = load_dotenv('RECO_URL')
RECO_TOKEN = load_dotenv('RECO_TOKEN')

INDONESIAN_URL = load_dotenv('INDONESIAN_URL')
INDONESIAN_TOKEN = load_dotenv('INDONESIAN_TOKEN')

# url = RECO_URL
# token = RECO_TOKEN
tableName = "course_ratings"
url = INDONESIAN_URL
token = INDONESIAN_TOKEN
pageNum = 1
numData = 30
total_pages = 0
uptoPage = 10
r = requests.get(url + tableName,
                  params = {
                      "page": pageNum,
                      "size": numData
                  },
                  headers = {
                      "Authorization": "token "+ token
                  })

resp = r.json()
# print("response is: \n", resp)

