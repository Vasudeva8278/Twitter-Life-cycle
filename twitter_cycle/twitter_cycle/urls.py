# urls.py
from django.contrib import admin
from django.urls import path, include
from social.views import RegisterView, CustomLoginView ,home_page_view # Import the custom login view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('social.urls')),  # Include other app URLs
    path('reg/', RegisterView.as_view(), name='reg'),  # Register view
    path('login/', CustomLoginView.as_view(), name='login_template'),  # Custom login view
    path('home/', home_page_view, name='home_page'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),  # JWT login endpoint
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Token refresh view
]
