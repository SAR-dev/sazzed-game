from django.db import models
from django.core.validators import RegexValidator
from utils.generators import generate_unique_slug
from django.dispatch import receiver
from django.db.models.signals import pre_save

from django.contrib.auth import get_user_model
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(max_length=50 ,unique=True, validators=[
        RegexValidator(
            regex='^[a-z0-9_-]{3,50}$',
            message="Invalid slug format! Slug should be between 3-50 characters. Use hyphen '-' or underscore '_' between letters if needed. ",
        ),
    ])
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.name)

@receiver(pre_save, sender=Tag)
def unique_slug(sender, instance, *args, **kwargs):
    if len(instance.slug) == 0:
        instance.slug = generate_unique_slug(Tag, instance.name)