from django.urls import path
from Blog_App import views

app_name = 'Blog_App'

urlpatterns = [
   path('',views.blog_list,name='index') ,
]
