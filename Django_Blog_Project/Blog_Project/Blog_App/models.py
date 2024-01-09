from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserBlog(models.Model):
    user = models.ForeignKey(User,related_name='user_blog',on_delete=models.CASCADE)
    slug = models.SlugField()
    blog_title = models.CharField(max_length=256)
    blog = models.TextField()
    blog_image = models.ImageField(upload_to='blog_pics')
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_title
    

class Comment(models.Model):
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    blog_comment = models.ForeignKey(UserBlog, on_delete=models.CASCADE)
    comments = models.TextField()

    def __str__(self):
        return self.comments
    

class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    blog_likes = models.ForeignKey(UserBlog,on_delete=models.CASCADE)