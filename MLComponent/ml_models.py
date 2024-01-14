# from courseRecoSystem.imports import dataImports
# from .imports import modelImports

from .models import PredictionsQuizDf,PredictionsAssnDf
from preprocessingComponent.models import CourseRatingPreprocessed
from courseRecoSystem.imports import dataImports

from surprise import Reader, Dataset
from surprise.model_selection import train_test_split, cross_validate, GridSearchCV
from surprise import KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline, SVD
from surprise import accuracy
from surprise.dump import dump
import pandas as pd
import random


def trainset_and_testset_rating(): 
    
    rating = pd.DataFrame.from_records(CourseRatingPreprocessed.objects.all().values('student', 'course_code', 'rating'))

    reader = Reader(rating_scale=(0,5))
    data = Dataset.load_from_df(rating,reader)
    raw_ratings = data.raw_ratings

    
    random.shuffle(raw_ratings)
    threshold = int(len(raw_ratings)*0.8)
    train_raw_ratings = raw_ratings[:threshold]
    test_raw_ratings = raw_ratings[threshold:]
    data.raw_ratings = train_raw_ratings
    trainset = data.build_full_trainset()
    testset = data.construct_testset(test_raw_ratings)
    testset = trainset.build_anti_testset() 

    return trainset, testset
    
def trainset_and_testset_quiz():     

    quiz = pd.read_pickle("quiz.pkl")

    reader_quiz = Reader(rating_scale=(0,5))
    data_quiz = Dataset.load_from_df(quiz,reader_quiz)
    trainset = data_quiz.build_full_trainset()

    
    raw_marks_quiz = data_quiz.raw_ratings
    random.shuffle(raw_marks_quiz)
    threshold = int(len(raw_marks_quiz)*0.8)
    train_raw_quiz_marks = raw_marks_quiz[:threshold]
    test_raw_quiz_marks = raw_marks_quiz[threshold:]
    data_quiz.raw_ratings = train_raw_quiz_marks
    trainset = data_quiz.build_full_trainset()
    testset = data_quiz.construct_testset(test_raw_quiz_marks)
    testset = trainset.build_anti_testset()

    return trainset, testset


def trainset_and_testset_assn(): 

    assignment = pd.read_pickle("assignment.pkl")

    reader_assignment = Reader(rating_scale =(0,5))
    data_assignment = Dataset.load_from_df(assignment,reader_assignment)
    raw_assignment = data_assignment.raw_ratings
    trainset = data_assignment.build_full_trainset()

    random.shuffle(raw_assignment)
    threshold = int(len(raw_assignment)*0.8)
    train_raw_assignment = raw_assignment[:threshold]
    test_raw_assignment = raw_assignment[threshold:]
    data_assignment.raw_ratings = train_raw_assignment
    trainset = data_assignment.build_full_trainset()
    testset = data_assignment.construct_testset(test_raw_assignment)
    testset = trainset.build_anti_testset()
    
    return trainset, testset




def train_and_test_svdModel(trainset, testset, model_for): 
    model = SVD(n_factors=10,n_epochs=20,lr_all=0.005,reg_all=0.2)
    model.fit(trainset)
    
    dump(file_name = f"{dataImports.SVDModelsFolder}/SVD_model.pkl", algo = model)
    predictions_records = {"status": "SVD Model saved"}
    return predictions_records

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import sklearn
import pickle
from numba import jit, cuda
from preprocessingComponent.models import CourseInfoPreprocessed

@jit(target_backend = 'cuda')
def makeCosineSimAndIndices(): 
    data_course_list = pd.DataFrame.from_records(CourseInfoPreprocessed.objects.all().values())
    _df = data_course_list
    based_on_col = "tag"
#   indices = pd.Series(_df.index,index=_df["id"])
    indices=pd.Series(range(0, data_course_list['course_name'].size),index = data_course_list['course_name'].tolist())

    count: sklearn.feature_extraction.text.TfidfVectorizer =TfidfVectorizer()
    count_matrix = count.fit_transform(_df[based_on_col])
    cosine_sim = cosine_similarity(count_matrix,count_matrix)

    storeAsPkl(indices, "models/content_based/indices.pkl")
    storeAsPkl(cosine_sim, "models/content_based/cosineSim.pkl")
    return {"status": "models built"}

def storeAsPkl(data, path): 
    f = open(path, "wb")
    pickle.dump(data, f)
    f.close()


from libreco.data import random_split, DatasetPure
from libreco.algorithms import NCF
from libreco.evaluation import evaluate
import tensorflow as tf
def buildModelForNCF(): 
    rating = pd.DataFrame.from_records(CourseRatingPreprocessed.objects.all().values('student', 'course_code', 'rating'))
    rating_cpy = rating.copy()
    rating_cpy.columns = ['user','item','label']
    train_data_full, data_info_full= DatasetPure.build_trainset(rating_cpy)

    tf.compat.v1.reset_default_graph()
    model1 = NCF(task="rating",data_info=data_info_full,loss_type="cross_entropy",embed_size= 8,n_epochs=30,lr=1e-3,batch_size=16,num_neg=1,)

    model1.fit(train_data_full,neg_sampling=False, verbose = 2,metrics=["loss","rmse"],)

    data_info_full.save(f"{dataImports.NCFModelsFolder}/data_info_rating",model_name='ncfModelRating')
    model1.save(f"{dataImports.NCFModelsFolder}/model_rating",model_name='ncfModelRating')

    return {"status": "NCF Model and data_info saved"}