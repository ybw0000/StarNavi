from accounts.models import User
from rest_framework import serializers
from .models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    liked = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class FieldsForAnalyticSerializer(serializers.Serializer):
    user = serializers.PrimaryKeyRelatedField(queryset=Like.objects.all())
    post = serializers.PrimaryKeyRelatedField(queryset=Like.objects.all())


class AnalyticSerializer(serializers.ModelSerializer):
    like = serializers.SerializerMethodField('get_like')

    class Meta:
        model = Like
        fields = ('created', 'like')

    def get_like(self, obj):
        likes = Like.objects.filter(created=obj.created)
        serializer = FieldsForAnalyticSerializer(likes, many=True)
        return serializer.data
