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