from django.urls import path
from App_Login import views

app_name ='App_Login'

urlpatterns = [
    path('signup/', views.signup, name= 'signup'),
    path('login/',views.login_req,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile_page,name='profile'),
    path('update_profile/',views.update_profile,name='update_profile'),
    path('change_password/',views.change_password,name='change_password'),
    path('update_profile_picture',views.update_profile_picture, name = 'update_profile_picture'),
    path('upload_profile_picture',views.upload_profile_picture, name = 'upload_profile_picture'),
]