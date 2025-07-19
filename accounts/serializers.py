from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            is_active=True
        )
        return user
    

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
     def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            # request=self.context.get('request'),
            username=username,
            password=password
        )
        user = authenticate(username=username, password=password)

        print("CustomTokenObtainPairSerializer validate called", user )
        if not user:
            raise serializers.ValidationError({"error": "Invalid username or password."})

        if not user.is_active:
            raise serializers.ValidationError({"error": "This account is inactive."})

        if user.is_superuser:
            raise serializers.ValidationError({"error": "You are not allowed to login."})

        # Set self.user so super().validate can use it
        self.user = user

        return super().validate(attrs)
    # def validate(self, attrs):
    #     data = super().validate(attrs)
    #     # Check if the user is a staff/admin
    #     if self.user.is_staff or self.user.is_superuser:
    #         # raise serializers.ValidationError("You are not allowed to login.")
    #         raise serializers.ValidationError({
    #             "error": "You are not allowed to login."
    #         })

    #     return data


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']