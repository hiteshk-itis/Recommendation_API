from .models import PredictionsRatingDf,PredictionsQuizDf,PredictionsAssnDf
from preprocessingComponent.models import CourseRatingPreprocessed

from surprise import Reader, Dataset
from surprise.model_selection import train_test_split, cross_validate, GridSearchCV
from surprise import KNNBasic, KNNWithMeans, KNNWithZScore, KNNBaseline, SVD
from surprise import accuracy

import pandas as pd
import random


def trainset_and_testset_rating(): 
    
    rating = pd.DataFrame.from_records(CourseRatingPreprocessed.objects.all().values())

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
     
    if model_for == "rating": 
        model_df = PredictionsRatingDf
    elif model_for == "quiz": 
        model_df = PredictionsQuizDf
    elif model_for == "assn": 
        model_df = PredictionsAssnDf
    else: 
        raise Exception('`model_for` param got unexpected val: ', model_for)

    model = SVD(n_factors=10,n_epochs=20,lr_all=0.005,reg_all=0.2)
    model.fit(trainset)
    
    # build_anti_testset() user-item matrix of all the items not interacted by user 
    
    predictions = model.test(testset)
    predictions_df = pd.DataFrame(predictions)
    
    predictions_records = predictions_df.to_dict('records')
    
    if len(model_df.objects.all()): 
        model_df.objects.all().delete()

    model_instances = [
        model_df(
            uid = predictions_record['uid'], 
            iid = predictions_record['iid'], 
            r_ui = predictions_record['r_ui'], 
            est = predictions_record['est'], 
            details = predictions_record['details'], 
        )
        for predictions_record in predictions_records
    ]
    model_df.objects.bulk_create(model_instances)
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
