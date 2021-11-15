from django.shortcuts import render, redirect
from .models import Post, Category
from .forms import PostForm
from django.db.models import Q

# Create your views here.
def index (request):
    q = request.GET.get('q')     if request.GET.get('q') != None else ' '
    posts = Post.objects.filter(Q(category__name__icontains= q) |
                    Q(title__icontains=q) |
                     Q(description__icontains=q) )
    categories = Category.objects.all()
    posts_count = posts.count()
    context = {
        'posts':posts,
        'categories':categories,
        'posts_count':posts_count
        
    }
    return render(request, 'Post/index.html', context )

    

def detail(request, pk):
    post=Post.objects.get(id=pk)
    context={
        'post':post
    }
    return render(request, 'Post/detail.html', context)

def createPost(request):
    form= PostForm()
    if request.method == 'POST':
        form=PostForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
    context={
            'form':form
        }
    return render(request, 'Post/add_post.html', context)

def UpdatePost(request, pk):
    post=Post.objects.get(id=pk)
    form=PostForm(instance=post)
    if request.method=='POST':
        form=PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={
        'form':form
    }
    return render(request, 'Post/update_post.html', context)
        
def deletePost(request,pk):
    post=Post.objects.get(id=pk)
    if request.method=='POST':
        post.delete()
        return redirect('index')
    return render(request, 'Post/delete_post.html', {'obj':post})


