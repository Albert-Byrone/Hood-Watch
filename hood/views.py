from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate
from django.contrib.auth.decorators import login_required
from .models import Profile,NeighbourHood,Post,Business
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostForm,UpdateProfileForm,NeighbourHoodForm,BusinessForm,SignupForm


@login_required(login_url='/accounts/login')
def index(request):
    posts = Post.objects.all()
    posts = posts[::-1]
    print(posts,"nnnnnnnnnnnnnn")
    return render(request,'main/index.html',{"posts":posts})


# Create your views here.
