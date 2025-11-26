from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
# example: register a viewset later
# router.register(r'properties', views.PropertyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]