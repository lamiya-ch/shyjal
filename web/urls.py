from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.index,name='index'),
   path("projects",views.projects,name='projects'),
   path("features",views.features,name='features'),
   path("writtings",views.writtings,name='writtings')
]