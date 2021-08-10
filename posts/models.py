from django.db import models
from accounts.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
    text = models.TextField(max_length=1000, blank=False)
    pub_date = models.DateTimeField(auto_now_add=True)
    liked = models.ManyToManyField(User, blank=True, related_name='liked')

    def __str__(self):
        return str(self.id)

    @property
    def num_likes(self):
        return self.liked.all().count()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.post_id)
