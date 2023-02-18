from django.contrib import admin
from django.urls import path, include
from . import views
from . views import UserViewSet
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
