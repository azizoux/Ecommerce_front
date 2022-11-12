from django.urls import path, include
from rest_framework import routers

from .views import MugViewSet, CartViewSet

router = routers.DefaultRouter()
router.register('mugs', MugViewSet)
router.register('carts', CartViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
