from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostLikeView, PostCommentView , PostTagListView 

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('new/', PostCreateView.as_view(), name='new_post'),
    path('p/<uuid:pk>/', PostDetailView.as_view(), name='details'),
    path('p/<uuid:pk>/like', PostLikeView, name='like'),
    path('p/<uuid:pk>/comment', PostCommentView, name='comment'),
    path('p/<uuid:pk>/edit', PostUpdateView.as_view(), name='update_post'),
    path('p/<uuid:pk>/delete', PostDeleteView.as_view(), name='delete_post'),
    path('p/tag/<str:tag>', PostTagListView.as_view(), name='tag'),
]
