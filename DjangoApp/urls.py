from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userApi/', include('UserApi.urls')),
    path('menuApi/', include('MenyuApi.urls')),
    path('menu/', include('Menyu.urls')),
    path('', include('Users.urls')),
]
