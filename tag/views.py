from rest_framework import generics
from .models import Tag
from .serializers import TagSerializer
from utils.paginations import PazeSizePagination

class TagListView(generics.RetrieveAPIView):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = PazeSizePagination