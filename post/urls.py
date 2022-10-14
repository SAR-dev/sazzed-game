from django.urls import path

from .views import PostListView, PostRetriveView

app_name = 'post'

urlpatterns = [
	path('', PostListView.as_view(), name='post-list'),
	path('<int:pk>/', PostRetriveView.as_view(), name='post-retrive'),
]