from django.urls import path
from .views import ImageCreateView

app_name = 'image'

urlpatterns = [
    path('create/', ImageCreateView.as_view(), name='image-create'),
]