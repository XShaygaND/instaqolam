from django.urls import path, include

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetailView.as_view(), name='details'),
    path('new/', PostCreateView.as_view(), name='new_post'),
]
