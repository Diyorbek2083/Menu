from django.contrib import admin
from django.urls import path, include, re_path
from .views import UserView
from .documentation import schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView, basename='users')



urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
