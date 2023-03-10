from rest_framework.viewsets import ModelViewSet

from home.models import Category, Product
from home.serializers import CategoryModelSerializer, ProductModelSerializer, CartModelSerializer


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer


class ProductModelViewSet(ModelViewSet):
    """
    CRUD products
    """
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
