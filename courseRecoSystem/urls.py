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
from courseRecoOne import urls as courseRecoOne_urls    
from studentData import urls as std_urls    
from preprocessingComponent import urls as pc_urls
# from MLComponent import urls as ml_urls    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('courseRecoOne.urls')),
    path('api/', include(std_urls)),
    # path('api/', include(ml_urls)),
    path('api/', include(pc_urls)),

]
