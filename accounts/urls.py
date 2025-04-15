from django.urls import re_path
from . import views
from django.urls import path
from .views import CookieTokenObtainPairView, CookieTokenRefreshView, logout_user

urlpatterns = [
    re_path('signup/', views.signup, name='signup'),
    path('logout/', logout_user, name='logout'),
    path('token/', CookieTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CookieTokenRefreshView.as_view(), name='token_refresh'),
]