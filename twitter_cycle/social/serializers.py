from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile,Post,Like,Comment,Share

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    

class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['user','bio','profile_image','followers']

class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    shares_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id','user','content','image','created_at','likes_count','shares_count','comments_count']

    def get_likes_count(self,obj):
        return obj.likes.count()
    def get_comments_count(self,obj):
        return obj.comments.count()
    def get_shares_count(self,obj):
        return obj.shares.count()
    
class Likeserializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    post = serializers.ReadOnlyField(source = 'post.id')

    class Meta:
        model = Like
        fields = ['user','post','created_at']


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = 'user.username')
    Post = serializers.ReadOnlyField(source='post.id')
    class Meta:
        model = Comment
        fields = ['user','post','content','created_at']


class ShareSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    post = serializers.ReadOnlyField(source='post.id')

    class Meta:
        model = Share
        fields = ['user', 'post','created_at']