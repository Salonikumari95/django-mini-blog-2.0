from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# 🏠 Ye function sabhi blog posts ko home page par dikhata hai
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  # Latest post sabse upar
    return render(request, 'posts/post_list.html', {'posts': posts})


# 📄 Ye function ek specific post ko detail page par dikhata hai
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})


# ✍️ Ye function naya blog post create karne ke liye hai
@login_required  # Sirf login user hi blog create kar sakta hai
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)  # form data + image handle karega
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # current logged-in user ko author bana rahe hain
            post.save()
            return redirect('home')  # create hone ke baad home page pe redirect
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


# 📝 Ye function existing blog ko edit karne ke liye hai
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Sirf apna blog edit kar sakta hai user
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})


# ❌ Ye function blog delete karne ke liye hai
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    # Sirf apna blog hi delete kar sakta hai
    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})


# 👤 Ye function user ke apne blogs dikhata hai (My Posts page)
@login_required
def user_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'posts/user_posts.html', {'posts': posts})
