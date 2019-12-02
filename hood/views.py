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

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = SignupForm()
    return render(request, 'registration/registration_form.html', {'form': form})

def home(request):
    all_hoods = NeighbourHood.objects.all()
    all_hoods=all_hoods[::-1]
    context={
        'all_hoods':all_hoods
    }
    return render(request,'main/home.html',context)

def create_hood(request):
    if request.method =="POST":
        form  = NeighbourHoodForm(request.POST,request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('home')
    else:
        form = NeighbourHoodForm()
    return render(request,'main/newhood.html',{'form':form})

def one_hood(request,id):
    hood = NeighbourHood.objects.get(id = id)
    buss = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            busin_form = form.save(commit=False)
            busin_form.neighbourhood = hood
            busin_form.user = request.user.profile
            busin_form.save()
            return redirect('single-hood', hood.id)
    else:
        form = BusinessForm()
    context ={
        'hood':hood,
        'business':buss,
        'posts':posts,
        'form':form,      
    }
    return render(request,'main/single_hood.html',context)

def hood_members(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    members = Profile.objects.filter(neighbourhood = hood)
    return render(request,'main/members.html',{'members':members})

def create_posts(request,hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood =hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood',hood.id)
    else:
        form =PostForm
    return render(request,'main/post.html',{'form':form})

def join_hood(request,id):
    neighbourhood = get_object_or_404(NeighbourHood,id=id)
    request.user.profile.neighbourhood=neighbourhood
    request.user.profile.save()
    return redirect('home')

def leave_hood(request,id):
    hood = get_object_or_404(NeighbourHood,id=id)
    request.user.profile.neighbourhood=None
    request.user.profile.save()
    return redirect('home')

def profile(request,username):
    return render(request,'profile/prof.html')

