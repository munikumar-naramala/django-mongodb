from django.urls import path, include
from rest_framework import routers
from .views import LogmongoViewSet

router = routers.DefaultRouter()
router.register(r'logmongo', LogmongoViewSet, basename='logmongo')

urlpatterns = [
    path('', include(router.urls)),
]
