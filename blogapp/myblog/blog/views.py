from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from rest_framework import viewsets
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .forms import CommentForm

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-date')
    serializer_class = PostSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-date')
    serializer_class = CommentSerializer

#Views
def index(request):
    return render(request, 'blog/blog.html')

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    id = str(post.id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return HttpResponseRedirect('/'+id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    id = str(post.id)
    post_pk = comment.post.pk
    comment.delete()
    return HttpResponseRedirect('/'+id)
