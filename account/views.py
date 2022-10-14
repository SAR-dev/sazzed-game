from rest_framework import generics, permissions
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import NotFound
from django.contrib.auth import get_user_model
from .serializers import UserUpdateSerializer, UserAvatarUpdateSerializer
User = get_user_model()

class MeRetriveView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserUpdateSerializer
    
    def get_object(self):
        try:
            return User.objects.get(id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)

class MeAvatarUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserAvatarUpdateSerializer
    
    def get_object(self):
        try:
            return User.objects.get(id=self.request.user.id)
        except ObjectDoesNotExist:
            raise NotFound(detail="Error 404, Not Found!", code=404)