from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from utils.paginations import PazeSizePagination
from django_filters import rest_framework as filters

class PostFilter(filters.FilterSet):
    o = filters.OrderingFilter(
        fields=(
            ('created_at', 'created_at'),
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author__username': ['exact'],
            'category__slug': ['exact'],
            'tags__slug': ['exact'],
        }

class PostListView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()
    pagination_class = PazeSizePagination
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PostFilter

class PostRetriveView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.published.all()