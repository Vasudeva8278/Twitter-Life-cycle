from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserprofileSerializer,PostSerializer,Likeserializer,CommentSerializer,ShareSerializer
from django.db.models import Q
from django.views import View
from django.contrib.auth.models import User
from .models import UserProfile, Post, Like, Share, Comment

# Create your views here.
class CustomLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    template_name = 'register.html'

    def get(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        return render(request, self.template_name, {'serializer': serializer})

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.POST)
        if serializer.is_valid():  # Corrected from 'is_vaild' to 'is_valid'
            serializer.save()
            
            # Redirect or return a success message
            return render(request, 'login.html')  # Redirect to a success page or home
        return render(request, self.template_name, {'serializer': serializer})


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

