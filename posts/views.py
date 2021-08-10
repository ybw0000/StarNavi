import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, AnalyticSerializer
from .forms import CreatePostForm


class FeedView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated, )
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        form = CreatePostForm(self.request.data)
        if form.is_valid():
            user = self.request.user
            user.last_activity = datetime.datetime.now()
            user.save()
            post = form.save(commit=False)
            post.author = self.request.user
            post.save()
        return Response(status=status.HTTP_201_CREATED)


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        user = request.user
        post_id = request.POST['post_id']
        post = Post.objects.get(id=post_id)

        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)

        like, created = Like.objects.get_or_create(
            user=user,
            post=post
        )
        user.last_activity = datetime.datetime.now()
        user.save()
        like.save()

        return Response(status=status.HTTP_200_OK)


class LikeView(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self, request, *args, **kwargs):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        likes = Like.objects.filter(created__gte=date_from, created__lte=date_to).distinct('created')
        queryset = AnalyticSerializer(likes, many=True)

        return Response(queryset.data, status=status.HTTP_200_OK)
