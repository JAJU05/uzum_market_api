from django.urls import path, include
from rest_framework.routers import DefaultRouter

from home.views import ProductModelViewSet, CategoryModelViewSet

router = DefaultRouter()
router.register('products', ProductModelViewSet, 'products')
router.register('category', CategoryModelViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
]
