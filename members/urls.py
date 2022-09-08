from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import UserCreateView, UserLoginView, UserDetailView, UserProfileUpdateView

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('u/<slug:slug>/', UserDetailView.as_view(), name='profile'),
    path('u/<slug:slug>/edit_profile/', UserProfileUpdateView.as_view(), name='edit_profile'),
]
