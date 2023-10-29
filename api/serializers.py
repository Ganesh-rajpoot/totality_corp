from rest_framework import serializers
from .models import UserDetails
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = '__all__'
    
    def validate_phone(self, value):
        if len(str(value)) > 10:
            raise serializers.ValidationError("Mobile number must be 10 digits")
        return value
    
