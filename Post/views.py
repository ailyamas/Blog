from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def index (request):
    posts = Post.objects.all()
    context = {
        'posts':posts
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
