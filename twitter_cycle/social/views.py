from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import RegisterSerializer,UserprofileSerializer,PostSerializer,Likeserializer,CommentSerializer,ShareSerializer
from django.db.models import Q
from rest_framework.views import APIView
from django.views import View
from django.contrib.auth.models import User
from .models import UserProfile, Post, Like, Share, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
class CustomLoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page.html')  # Redirect to home_page.html on successful login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class CustomerLogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('login')
class RegisterView(View):
    template_name = 'register.html'

    def get(self, request):
        serializer = RegisterSerializer()
        return render(request, self.template_name, {'serializer': serializer})

    def post(self, request):
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect('success')  # Redirect to a success page or login
        return render(request, self.template_name, {'serializer': serializer})

@login_required
def home_page_view(request):
    posts = Post.objects.all().order_by('-created_at')  # Fetch posts, ordered by newest first
    likes = Like.objects.all()
    comments = Comment.objects.all()
    shares = Share.objects.all()

    context = {
        'posts': posts,
        'likes': likes,
        'comments': comments,
        'shares': shares,
    }
    return render(request, 'home_page.html', context)



@login_required
def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Like.objects.create(user=request.user, post=post)
    return redirect('home_page')

@login_required
def comment_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content')
    Comment.objects.create(user=request.user, post=post, content=content)
    return redirect('home_page')

@login_required
def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    Share.objects.create(user=request.user, post=post)
    return redirect('home_page')








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

