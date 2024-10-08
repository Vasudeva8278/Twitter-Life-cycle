from django.urls import path
from . import views
from .views import UserprofileDetailview,UserProfileListview,LikeDetailView,LikeListView,CommentDetailView,CommentListView,ShareDetailView,ShareListView,PostDetailView,PostListView

urlpatterns = [
    path('', views.home, name='home'),
    path('userlist/', UserProfileListview.as_view(),name='userlist'),
    path('profiledetails/<str:user__username>/',UserprofileDetailview.as_view(),name='profile_details'),
    path('Posts/<str:user__username>',PostListView.as_view(),name="posts"),
    path('postdetails/',PostDetailView.as_view(),name="postdetails"),
    path('likes/',LikeListView.as_view(),name='likes'),
    path('likedetails',LikeDetailView.as_view(),name='likedetails'),
    path('coments/',CommentListView.as_view(),name='comments'),
    path('commentsdetails',CommentDetailView.as_view(),name='commentsdetails'),
    path('shares/',ShareListView.as_view(),name='shares'),
    path('sharedetails/',ShareDetailView.as_view(),name='sharedetails')

]
