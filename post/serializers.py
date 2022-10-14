from account.serializers import UserSerializer
from category.serializers import CategorySerializer
from image.serializers import ImageSerializer
from rest_framework import serializers
from tag.serializers import TagSerializer

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    author = UserSerializer()
    
    class Meta:
        model = Post
        fields = ['id',
            'title', 
            'version',
            'content', 
            'cover', 
            'images', 
            'category', 
            'tags', 
            'play_link',
            'play_downloads',
            'play_code',
            'amazon_link',
            'amazon_downloads',
            'amazon_code',
            'status', 
            'author', 
            'created_at', 
            'updated_at']