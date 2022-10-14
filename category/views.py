from rest_framework import generics
from .models import Category
from .serializers import CategorySerializer
from utils.paginations import PazeSizePagination

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = PazeSizePagination