from django.shortcuts import render

from django.http import HttpResponse 
from django.http import HttpRequest as request

from rest_framework import viewsets
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .retrieveRawTables import retrieveTables, retrieveSingleTable
from .preprocessTables import preprocessTables
import json
from .realTimeDbUpdate import *
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def retrieve_singleTable(request, tableName): 
    status = retrieveSingleTable(tableName)
    return HttpResponse(json.dumps(status), content_type='application/json')


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def preprocessRawTables(request, tableName): 
    status = preprocessTables(tableName)
    return HttpResponse(json.dumps(status), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def batchUpdate(request): 
    status_raw = retrieveAllRawTables()
    status_preprocess = preprocessAllRawTables()
    status_model = modelForAllAlgorithms()
    status = {
        "raw Tables Retrieved": status_raw, 
        "raw Tables preprocessed": status_preprocess, 
        "modeling done": status_model
    }
    return HttpResponse(json.dumps(status), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def preprocessAllTables(request): 
    # status_raw = retrieveAllRawTables()
    status_preprocess = preprocessAllRawTables()
    # status_model = modelForAllAlgorithms()
    status = {
        # "raw Tables Retrieved": status_raw, 
        "raw Tables preprocessed": status_preprocess, 
        # "modeling done": status_model
    }
    return HttpResponse(json.dumps(status), content_type='application/json')

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def buildAllModels(request): 
    # status_raw = retrieveAllRawTables()
    status_build = modelForAllAlgorithms()
    # status_model = modelForAllAlgorithms()
    status = {
        # "raw Tables Retrieved": status_raw, 
        "build models": status_build, 
        # "modeling done": status_model
    }
    return HttpResponse(json.dumps(status), content_type='application/json')