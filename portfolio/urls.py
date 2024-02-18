# new
from django.urls import path
from .views import index,download_file

urlpatterns = [
    path('',index,name='home'),
    path('download-resume/', download_file, name='download_resume'),
]