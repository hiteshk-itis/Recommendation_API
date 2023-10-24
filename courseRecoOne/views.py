from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
 
from .serializers import HeroSerializer, CourseAnalyticsSerializer, CourseInfoSerializer, CourseRatingSerializer, KeywordsSerializer, TagsSerializer, ServerCourseSerializer, CourseNameSerializer, CourseListSerializer, UserListSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Hero, CourseAnalytics, CourseInfo, CourseRating, Keywords, Tags, ServerCourse, CourseList, UserList
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class UserListViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = UserList.objects.all().order_by('id')
    serializer_class = UserListSerializer


class CourseAnalyticsViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CourseAnalytics.objects.all().order_by('id')
    serializer_class = CourseAnalyticsSerializer

class CourseInfoViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CourseInfo.objects.all().order_by('id')
    serializer_class = CourseInfoSerializer

class CourseListViewSet(viewsets.ModelViewSet): 
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CourseList.objects.all().order_by('id')
    serializer_class = CourseListSerializer

class CourseNameViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = CourseInfo.objects.all().order_by('id')
    serializer_class = CourseNameSerializer

class CourseRatingViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]   

    queryset = CourseRating.objects.all().order_by('rating_id')
    serializer_class = CourseRatingSerializer

class KeywordsViewSet(viewsets.ModelViewSet):
    queryset = Keywords.objects.all().order_by('id')
    serializer_class = KeywordsSerializer

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tags.objects.all().order_by('id')
    serializer_class = TagsSerializer

class ServerCourseViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = ServerCourse.objects.all().order_by('id')
    serializer_class = ServerCourseSerializer


