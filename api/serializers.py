from rest_framework import serializers
from django.contrib.auth.models import User
from posts.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'username']


class PostSerializer(serializers.ModelSerializer):
    #auther = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'auther', 'title', 'body', 'created', 'updated']
        #depth = 1
