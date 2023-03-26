from django.urls import path
from . import views



urlpatterns = [
    path('',views.port),
    path('download-resume/', views.download_resume, name='download-resume'),

]