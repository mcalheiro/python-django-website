from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project/<pk>', views.project, name='project'),
    path('create-project/', views.createProject, name='create-project'),
]
