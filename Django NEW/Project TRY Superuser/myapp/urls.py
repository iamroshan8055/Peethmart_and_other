from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse
from . import views
from django.contrib.auth.models import User
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    # path('parent/', views.ParentList.as_view(),name="parentlist"),
    # path('get_object/', views.ParentDetail.get_object,name="get_object"),
    # path('get_all/', views.ParentDetail.get_all,name="get_all"),

    path('post', views.UserDetail.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),

    path('auth/login',views.LoginPage.as_view()),

    # path('get/<int:pk>/', views.ParentDetail.get,name="get"),
    # path('put/<int:pk>/', views.ParentDetail.put,name="put"),
    # path('delete/<int:pk>/', views.ParentDetail.delete,name="delete"),
]

urlpatterns = format_suffix_patterns(urlpatterns)