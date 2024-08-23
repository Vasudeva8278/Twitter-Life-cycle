from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    followers = models.ManyToManyField(User, related_name='following', blank=True)

    def __str__(self):
        return self.user.username

    def total_posts(self):
        return self.user.posts.count()

    def total_followers(self):
        return self.followers.count()

    def total_following(self):
        return self.user.following.count()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='posts')
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}:{self.content[:30]}'
    
    def total_likes(self):
        return self.likes.count()
    def total_comments(self):
        return self.comments.count()
    def total_shares(self):
        return self.shares.count()
    

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'post')

    def __str__(self):
        return f'{self.user.username} liked {self.post.content[:20]}'
    
class Share(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='shares')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} shared {self.post.content[:20]}'
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} commented on {self.post.content[:20]}'