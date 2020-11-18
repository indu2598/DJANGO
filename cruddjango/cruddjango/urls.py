"""cruddjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers
from rest_framework import routers, serializers, viewsets
from myapp import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view =  get_swagger_view(title= "Crud Swagger" )
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSets)
router.register(r'groups', views.GroupViewSets)
router.register(r'tasks', views.TaskViewSets)



urlpatterns = [
    # url(r"^$",schema_view),
    path('', include(router.urls)),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/',views.TaskGenericSet.as_view()),
     path('api/<int:pk>',views.TaskGenericViewset.as_view()),
]
