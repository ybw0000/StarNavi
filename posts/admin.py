from django.contrib import admin
from .models import Post, Like
from django.contrib.auth.models import Group

admin.site.register(Post)
admin.site.register(Like)

admin.site.unregister(Group)

