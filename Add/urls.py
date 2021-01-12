from django.urls import path
from .views import *
from . import views
app_name = 'Add'

urlpatterns = [
    #add
    path('add/',views.Index.as_view(), name="index"),
    path('add/client',views.AddClient.as_view(), name="add.client"),
    path('download/<str:url>',views.Download.as_view(), name="index"),
]