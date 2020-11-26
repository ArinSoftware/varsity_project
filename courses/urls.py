from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='courses'),
    path('<int:course_id>', views.course, name='course'),
]