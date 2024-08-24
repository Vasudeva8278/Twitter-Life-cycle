from django.contrib import admin
from .models import UserProfile,Post,Like,Comment,Share

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Share)