from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .documentation import schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserView, basename='users')
router.register(r'rooms', views.RoomView, basename='rooms')
router.register(r'table', views.TableView, basename='table')



urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
