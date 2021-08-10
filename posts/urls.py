from django.urls import path
from .views import FeedView, PostCreate, PostDetail, LikeView

urlpatterns = [
    path('', FeedView.as_view(), name='feed'),
    path('<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('<int:pk>/like/', PostDetail.as_view(), name='post-like'),
    path('create/', PostCreate.as_view(), name='create-post'),
    path('likes/', LikeView.as_view(), name='analytics')
]