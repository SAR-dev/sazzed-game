import os
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
from django.utils.deconstruct import deconstructible
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit

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


class Image(models.Model):
    image = ProcessedImageField(upload_to=save_image,
                                processors=[ResizeToFit(width=1400)],
                                format='JPEG',
                                options={'quality': 80},
                                height_field='height',
                                width_field='width')
    height = models.IntegerField(blank=True)
    width = models.IntegerField(blank=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        return str(self.image)
