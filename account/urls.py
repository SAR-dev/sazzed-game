from django.urls import path
from .views import MeRetriveView, MeAvatarUpdateView

app_name = 'account'

urlpatterns = [
	path('me/', MeRetriveView.as_view(), name='me'),
	path('avatar/', MeAvatarUpdateView.as_view(), name='avatar'),
]