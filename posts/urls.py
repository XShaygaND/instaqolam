from django.urls import path, include

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('p/<int:pk>/', PostDetailView.as_view(), name='details'),
    path('new/', PostCreateView.as_view(), name='new_post'),
    path('p/<int:pk>/edit', PostUpdateView.as_view(), name='update_post'),
    path('p/<int:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
]
