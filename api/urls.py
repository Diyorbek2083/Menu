from django.contrib import admin
from django.urls import path, include
from .views import PostApi
from .documentation import schema_view
urlpatterns = [
    path('', PostApi.as_view())
]
