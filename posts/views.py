from django.shortcuts import render,get_object_or_404
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from posts.models import Post
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
class IndexView(LoginRequiredMixin,generic.TemplateView):
    template_name="posts/welcome.html"

class UserPostList(LoginRequiredMixin,generic.ListView):
    model=Post
    template_name='posts/user_posts.html'
    context_object_name='posts'

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user)

class UserPostDetail(LoginRequiredMixin,generic.DetailView):
    model=Post

class UserPostCreate(LoginRequiredMixin,generic.CreateView):
    model=Post
    fields=("title","complete")

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class UserPostUpdate(LoginRequiredMixin,UserPassesTestMixin,generic.UpdateView):
    model=Post
    fields=("title","complete")

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False


class UserPostDelete(LoginRequiredMixin,UserPassesTestMixin,generic.DeleteView):
    model=Post
    success_url=reverse_lazy('posts:user_index')
    


    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
