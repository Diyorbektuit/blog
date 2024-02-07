from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class PostSerializer(serializers.ModelSerializer):
    #author = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'created', 'updated']
        #depth = 1
