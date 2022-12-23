"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home import views as home_views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_swagger.views import get_swagger_view
from home import views as h_views

schema_view = get_schema_view(
    openapi.Info(
        title='Reporting Tool',
        default_version="v1",

    ),
    public=True,
    # permission_classes=(permissions.IsAuthenticated)
)

s_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path("swagger",schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path("about/",h_views.abount),
    path('admin/', admin.site.urls),
    path('sview/', s_view),

    path('',include('home.urls')),
]
