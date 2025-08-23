from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

# Registration serializer with explicit CharField usage
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.CharField(max_length=254)
    password = serializers.CharField(write_only=True)
    bio = serializers.CharField(required=False, allow_blank=True)
    profile_picture = serializers.CharField(required=False, allow_blank=True)

    def create(self, validated_data):
        # Explicitly use get_user_model().objects.create_user
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            bio=validated_data.get('bio', ''),
            profile_picture=validated_data.get('profile_picture', None)
        )
        Token.objects.create(user=user)
        return user

# Serializer for returning user data
class UserSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    username = serializers.CharField()
    email = serializers.CharField()
    bio = serializers.CharField()
    profile_picture = serializers.CharField()
    followers = serializers.CharField()  # You can serialize follower IDs or names as needed
