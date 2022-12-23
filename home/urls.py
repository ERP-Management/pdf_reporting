from django.contrib import admin
from django.urls import path
from home import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
# from rest_framework_swagger.views import get_swagger_view
# from django.conf.urls import url


schema_view = get_schema_view(
    openapi.Info(
        title='Reporting Tool',
        default_version="v1",

    ),
    # public=True,
    # permission_classes=(permissions.AllowAny)
)
urlpatterns = [
    # path("",views.index,name="home"),
    path("",schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path("about",views.abount,name="about"),
    path("student/<int:pk>",views.student_detail),
    path("stdList",views.student_get_all),
    # path('swagger',schema_view)
]

