from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userapi/', include('UserApi.urls')),
    path('menuapi/', include('MenyuApi.urls')),
    path('menu/', include('Menyu.urls')),
    path('', include('Users.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
