from django.shortcuts import render
from App_Login.forms import SignUpForm,ProfileUpdateForm,UpdateProfilePictureForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def signup(request):
    registered = False
    form = SignUpForm()
    if request.method =='POST':
        form = SignUpForm(data = request.POST)
        if form.is_valid():
            registered = True
            form.save()
            return HttpResponseRedirect(reverse("App_Login:login"))

    dictionary ={'title':'Sign Up','form':form}
    return render(request, 'App_Login/signup.html', context=dictionary)


def login_req(request):
    loged_in = False
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('App_Login:profile'))
            
    dictionary = {'title':'Login','loged_in':loged_in, 'form':form}
    return render(request,'App_Login/login.html',context=dictionary)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Login:login'))


@login_required
def profile_page(request):
    return render(request,'App_login/profile.html',context={'title':'Profile Page'})

@login_required
def update_profile(request):
    current_user = request.user
    form = ProfileUpdateForm(instance=current_user)
    if request.method == 'POST':
        form=ProfileUpdateForm(data=request.POST,instance = current_user)
        if form.is_valid():
            form.save()
            form= ProfileUpdateForm(instance = current_user)
            return HttpResponseRedirect(reverse('App_Login:profile'))
    dictionary={'title':'Update Profile','form':form}
    return render(request,'App_login/update_profile.html',context=dictionary)


@login_required
def change_password(request):
    current_user = request.user
    form=PasswordChangeForm(user=current_user)
    if request.method == 'POST':
        form=PasswordChangeForm(user=current_user,data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    dictionary  ={'title':'Change Password','form':form}
    return render(request,'App_login/change_password.html',context=dictionary)


@login_required
def update_profile_picture(request):
    current_user = request.user
    form = UpdateProfilePictureForm(instance = current_user.user_profile)
    if request.method == 'POST':
        form = UpdateProfilePictureForm(request.POST,request.FILES ,instance = current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:profile'))
    dictionary ={'title':'Update Profile Picture', 'form': form}
    return render(request,'App_Login.html/update_profile.html',context=dictionary)


@login_required
def upload_profile_picture(request):
    current_user = request.user
    form = UpdateProfilePictureForm()
    if request.method == 'POST':
        form = UpdateProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            user_obj = form.save(commit= False)
            user_obj.user = current_user
            form.save()

            return HttpResponseRedirect(reverse('App_Login:profile'))
    dictionary ={'title': 'Upload Profile Picture', 'form': form}
    return render(request,'App_Login/update_profile_pic.html',context=dictionary)