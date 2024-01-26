from django.shortcuts import render
from .models import Post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class PostListView(generic.ListView):
    model = Post
    template_name = "list.html"
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    template_name = "detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = "create.html"
    fields = ["title", "body"]

    def form_valid(self, form):
        form.instance.auther = self.request.user
        return super().form_valid(form)

