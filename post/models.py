import os
from uuid import uuid4

from category.models import Category
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.deconstruct import deconstructible
from image.models import Image
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from tag.models import Tag

User = get_user_model()

@deconstructible
class RenameAndRelocateImage(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        ext = filename.split('.')[-1]
        filename = '{}.{}'.format(uuid4().hex, ext)
        return os.path.join(self.path, filename)

save_image = RenameAndRelocateImage("images/")

class Post(models.Model):
    class PostPublished(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    class PostDraft(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='draft')

    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    content = models.TextField()
    cover = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80})
    images = models.ManyToManyField(Image, related_name='images', default=None, blank=True)
    tags = models.ManyToManyField(Tag, related_name='tags', default=None, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', default=None, blank=True)

    play_link = models.CharField(max_length=200)
    play_downloads = models.IntegerField()
    play_code = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80})

    amazon_link = models.CharField(max_length=200)
    amazon_downloads = models.IntegerField()
    amazon_code = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80})

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = PostPublished()
    draft = PostDraft()

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return str(self.title)