from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserprofileSerializer,PostSerializer,Likeserializer,CommentSerializer,ShareSerializer
from django.db.models import Q
from .models import UserProfile, Post, Like, Share, Comment
# Create your views here.
def home(request):
    return HttpResponse("welcome Preerthi")


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer


class UserProfileListview(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserprofileSerializer

class UserprofileDetailview(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserprofileSerializer
    lookup_field = 'user__username'

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class LikeListView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer

class LikeDetailView(generics.RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = Likeserializer
class CommentListView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
class CommentDetailView(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class ShareListView(generics.ListCreateAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer

class ShareDetailView(generics.RetrieveDestroyAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer


class ShareDetailView(generics.RetrieveDestroyAPIView):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer