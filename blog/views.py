# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import PostModel
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# objects.filter(topic__icontains=topic)
#     else:
#         posts = PostModel.objects.all()
#     return render(request, 'blog/index.html', {'posts': posts})
# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import PostModel

def index(request):
    query = request.GET.get('query')
    if query:
        posts = PostModel.objects.filter(title__icontains=query)
    else:
        posts = PostModel.objects.all()
    return render(request,'blog/index.html', {'posts': posts})
# blog/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# from .forms import BlogPostForm
from .models import BlogPost

# @login_required
# def create_post(request):
#     if request.method == 'POST':
#         form = BlogPostForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     else:
#         form = BlogPostForm()
#     return render(request, 'blog/create_post.html', {'form': form})

# @login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

# @login_required
def edit_post(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

# @login_required
def delete_post(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/delete_post.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(PostModel, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# blog/views.py

