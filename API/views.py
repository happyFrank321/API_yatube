from django.shortcuts import  get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, BasePermission
from rest_framework.response import Response

from .serializers import PostSerializer, CommentSerializer
from posts.models import Post, Comment


class CheckAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in ('DELETE', 'PUT', 'POST', 'PATCH'):
            return request.user == obj.author
        return True

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [CheckAuthor, IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [CheckAuthor, IsAuthenticated]


    def list(self, request, id):
        post = get_object_or_404(Post, pk=id)
        queryset = post.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

        def get_queryset(self):
            post = get_object_or_404(Post, id.kwargs.get('id'))
            comments = Comment.objects.filter(post_id=post.id)
            return comments

