from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title='Menyu sayt',
        default_version='v1',
        description='Api documentation',
        # terms_of_service="",
        contact=openapi.Contact(email='abdulazizilhomboyev2@gmail.com'),
        license=openapi.License(name='From Data Union')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
