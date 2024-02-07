from django.shortcuts import render
from rest_framework import generics
from posts.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly


class PostListAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
                          ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly,
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly

                          ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateAPIView(generics.UpdateAPIView):
    permission_classes = [
        IsAuthenticatedOrReadOnly,
        IsAuthorOrReadOnly
    ]
    queryset = Post.objects.all()
    serializer_class = PostSerializer