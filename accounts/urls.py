from django.urls import re_path
from . import views
from django.urls import path
from .views import MyTokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    re_path('signup', views.signup, name='signup'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]