from django.contrib import admin
from django.urls import path, include
from social.views import RegisterView  # Import the correct view class
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls')),  # Include other app URLs
    path('reg/', RegisterView.as_view(), name='reg'),  # Register view with .as_view()
    path('login/', TokenObtainPairView.as_view(), name='login'),  # Ensure trailing slash
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
