from django.shortcuts import render, redirect
from user.models import Dsuser
from .models import Post
from .forms import PostForm

# Create your views here.

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post_detail.html', {'post': post})


def upload(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = Dsuser.objects.get(pk=user_id)
            
            post = Post()
            post.title = form.cleaned_data['title']
            post.contents = form.cleaned_data['contents']
            post.image_url = form.cleaned_data['image_url']
            post.writer = user
            post.save()

            return redirect('/')
    else:
        form = PostForm()
        
    return render(request, 'upload.html', {'form': form})


def timeline(request):
    posts = Post.objects.all().order_by('-id')
    return render(request, 'timeline.html', {'posts': posts})