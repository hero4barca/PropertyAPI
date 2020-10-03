from django.urls import path, include
from rest_framework.routers import DefaultRouter
from PropertyApp import views

from rest_framework.urlpatterns import format_suffix_patterns

router = DefaultRouter()
router.register(r'properties', views.PropertyViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


