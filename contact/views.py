from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer
from utils.paginations import PazeSizePagination

class ContactCreateView(generics.CreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    pagination_class = PazeSizePagination