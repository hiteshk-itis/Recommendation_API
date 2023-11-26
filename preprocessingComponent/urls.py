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


# router.register(r'get_rec', views.ex_view, basename="get-rec")



urlpatterns = [     
    path('retrieve_single_table/<slug:tableName>', views.retrieve_singleTable), 
    path('preprocess_raw_tables/<slug:tableName>', views.preprocessRawTables), 
    path('batch_update', views.batchUpdate), 
    path('preprocess_all_tables/', views.preprocessAllTables),
    path('build_all_models/', views.buildAllModels)
    
]
