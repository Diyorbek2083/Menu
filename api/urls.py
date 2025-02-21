from django.contrib import admin
from django.urls import path, include, re_path
from .views import UserView,RoomViews,TableView,FoodcategoryView,FoodView,CommentView,ReplayCommentModelsView,LikeMolelsView,WaiterModelsView,UserModelsView,KarzinkaModelsView,DoimiyKarzinkaModelsView
from .documentation import schema_view
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserView, basename='users')
router.register(r'rooms',RoomViews , basename='rooms')
router.register(r'tables', TableView, basename='tables')
router.register(r'foodcategory', FoodcategoryView, basename='foodcategory')
router.register(r'foods', FoodView, basename='foods')
router.register(r'comments', CommentView, basename='comments')
router.register(r'replaycomments', ReplayCommentModelsView, basename='replaycomments')
router.register(r'likes', LikeMolelsView, basename='likes')
router.register(r'waiters', WaiterModelsView, basename='waiters')
router.register(r'usersinfo', UserModelsView, basename='usersinfo')
router.register(r'karzinka', KarzinkaModelsView, basename='karzinka')

router.register(r'doimiykarzinka', DoimiyKarzinkaModelsView, basename='doimiykarzinka')

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]



