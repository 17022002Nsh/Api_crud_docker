from django.urls import path
from .views import tudu_create_api


urlpatterns = [
    path('create/', tudu_create_api)
]
