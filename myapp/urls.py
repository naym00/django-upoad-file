from django.urls import path
from myapp.views import uploadFile, getFiles

urlpatterns = [
    path('get-files/', getFiles, name='get-files'),
    path('upload-file/', uploadFile, name='upload-file'),
]