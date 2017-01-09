from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from blog import views
from .models import Post, Comment

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="blog/blog.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name="blog/post.html")),
    url(r'^(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^about/', views.about, name="about"),
    url(r'^contact/', views.contact, name="contact"),
]
