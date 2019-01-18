"""basic_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('<int:pk>/', views.SchoolDetailsView.as_view(), name='details'),
    path('create/', views.SchoolCreateView.as_view(), name='create'),
    path('update/<int:pk>', views.SchoolUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', views.SchoolDeleteView.as_view(), name='delete'),
    
    
    # url(r'^(?P<pk>\d+)/$', views.SchoolDetailsView.as_view(), name='details'),
    # url(r'^create/$', views.SchoolCreateView.as_view(), name='school-create'),
    # url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='school-update'),
    # url(r'^delete/ (?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='school-delete'),
]

