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
# router.register(r'heroes', views.HeroViewSet)
router.register(r'course_analytics', views.CourseAnalyticsViewSet)
router.register(r'course_info', views.CourseInfoViewSet)
router.register(r'course_rating', views.CourseRatingViewSet)
router.register(r'keywords', views.KeywordsViewSet)
router.register(r'tags', views.TagsViewSet)
router.register(r'server_course', views.ServerCourseViewSet)
router.register(r'course_names', views.CourseNameViewSet)
router.register(r'course_list', views.CourseListViewSet)
router.register(r'user_list', views.UserListViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
