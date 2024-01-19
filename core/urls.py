"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,re_path,include

# external imported apps ->
# Swagger documentation
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#views
from process_data.views import get_all_activities, get_activities_by_date, get_activities_by_activity_name

schema_view = get_schema_view(
    openapi.Info(
        title="Strava-mod APIs",
        default_version='v1',
        description="APIs to fetch processed strava activities data",
        terms_of_service="https://yourapp.com/terms/",
        contact=openapi.Contact(email="uditpande2001@gmail.com"),
        license=openapi.License(name="Your License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('activities', get_all_activities, name="activities"),
#     path('activities_by_date', get_activities_by_date, name="get_activites_by_date"),
#     path('get_activities_by_activity_name', get_activities_by_activity_name, name="get_activities_by_activity_name")
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_activities/', get_all_activities, name="all_activities"),
    path('activities_by_date/', get_activities_by_date, name="get_activities_by_date"),
    path('activities_by_activity_name/', get_activities_by_activity_name, name="get_activities_by_activity_name"),

    # Swagger documentation
    path('swagger<str:format>', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]


