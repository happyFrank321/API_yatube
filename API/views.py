from django.shortcuts import render
from rest_framework import viewsets, request, status
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from rest_framework.response import Response

from .serializers import PostSerializer
from posts.models import Post


# Create your views here.
class PostsViewSet(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class DetailPostViewSet(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
