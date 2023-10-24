from django.shortcuts import render
from django.http import HttpResponse 
from django.http import HttpRequest as request

from rest_framework import viewsets
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ContentBasedFinalDfSerializer

from .content_based import content_based, SVD_rating, overall_SVD_rating #, SVD_quiz
from .content_based import NCF_rating_api

from .models import ContentBasedFinalDf
from . import ml_models

import json

import pandas as pd
from studentData.models import RefinedRating

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ContentBasedFinalDfViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ContentBasedFinalDf.objects.all().order_by('id')
    serializer_class = ContentBasedFinalDfSerializer
    

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def contentBasedRec(request, search_param):
    recommendations = content_based(search_param)
    return HttpResponse(json.dumps(recommendations), content_type='application/json')


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def SVDRatingRec(request, pk):
    recommendations = SVD_rating(pk)
    return HttpResponse(json.dumps(recommendations), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def OverallSVDRatingRec(request, num):
    recommendations = overall_SVD_rating(num)
    return HttpResponse(json.dumps(recommendations), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def SVDQuizRec(request, pk):
    recommendations = SVD_quiz(pk)
    return HttpResponse(json.dumps(recommendations), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def SVDAssnRec(request, pk):
    recommendations = content_based(pk)
    return HttpResponse(json.dumps(recommendations), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buildModel_forRating(request): 
    trainset, testset = ml_models.trainset_and_testset_rating()
    df_dict = ml_models.train_and_test_svdModel(trainset, testset, "rating")
    return HttpResponse(json.dumps(df_dict), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buildModel_forQuiz(request): 
    trainset, testset = ml_models.trainset_and_testset_quiz()
    df_dict = ml_models.train_and_test_svdModel(trainset, testset, "quiz")
    return HttpResponse(json.dumps(df_dict), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buildModel_forAssn(request): 
    trainset, testset = ml_models.trainset_and_testset_assn()
    df_dict = ml_models.train_and_test_svdModel(trainset, testset, "assn")
    return HttpResponse(json.dumps(df_dict), content_type='application/json')


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def NCFRatingRec(request, pk):
    
    recommendations = NCF_rating_api(pk)
    
    return HttpResponse(json.dumps(recommendations), content_type='application/json')
    
@api_view(['GET'])
def tempView(request): 
    return HttpResponse(json.dumps({"status": "temp json working"}), content_type='application/json')