from django.shortcuts import render

from django.http import HttpResponse 
from django.http import HttpRequest as request

from rest_framework import viewsets
from rest_framework.decorators import api_view, action, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .retrieveRawTables import retrieveTables
from .preprocessTables import preprocessTables
import json
# Create your views here.

@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def retrieveRawTables(request, tableName): 
    status = retrieveTables(tableName)
    return HttpResponse(json.dumps(status), content_type='application/json')


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def preprocessRawTables(request, tableName): 
    status = preprocessTables(tableName)
    return HttpResponse(json.dumps(status), content_type='application/json')