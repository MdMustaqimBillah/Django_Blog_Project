from django.shortcuts import render

# Create your views here.
def blog_list(request):
    return render(request,'Blog_App/index.html',context={})