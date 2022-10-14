from rest_framework import serializers
from .models import Contact
        
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['subject', 'message', 'type', 'first_name', 'last_name', 'email']