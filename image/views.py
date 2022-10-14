from django.shortcuts import render
from rest_framework import permissions, parsers, generics
from .serializers import ImageCreateSerializer, ImageSerializer
from .models import Image
from rest_framework import generics
from utils.paginations import PazeSizePagination

class ImageRetriveView(generics.RetrieveAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    pagination_class = PazeSizePagination

class ImageCreateView(generics.CreateAPIView):
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer
        
