from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('UserApi.urls')),
    path('menuapi/', include('MenyuApi.urls')),
    path('menu/', include('Menyu.urls')),
    path('', include('Users.urls')),
]
