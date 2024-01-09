from django.contrib import admin
from Blog_App.models import UserBlog, Comment, Like
# Register your models here.

admin.site.register(UserBlog)
admin.site.register(Comment)
admin.site.register(Like)