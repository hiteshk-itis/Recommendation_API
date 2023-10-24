"""
URL configuration for courseRecoSystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'ml', views.ContentBasedFinalDfViewSet)
# router.register(r'get_rec', views.ex_view, basename="get-rec")



urlpatterns = [
    path('', include(router.urls)), 
    path('build_model/rating/', views.buildModel_forRating),
    path('build_model/quiz/', views.buildModel_forQuiz),
    path('build_model/assignment/', views.buildModel_forAssn),

    path('get_recommendation/content_based/<int:search_param>/', views.contentBasedRec), 
    # path('get_recommendation/<slug:search_param>/', views.contentBasedRec), 

    path('get_recommendation/svd/rating/individual/<int:pk>/', views.SVDRatingRec), 
    path('get_recommendation/quiz/individual/<int:pk>/', views.SVDQuizRec), 
    path('get_recommendation/assignment/individual/<int:pk>/', views.SVDAssnRec), 
    path('get_recommendation/rating/overall/<int:num>', views.OverallSVDRatingRec),

    path('get_recommendation/ncf/rating/individual/<int:pk>/', views.NCFRatingRec), 

    path('get_recommendation/rating/individual/hybrid/<int:pk>/', views.SVDRatingRec), 
]
