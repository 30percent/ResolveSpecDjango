from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.views import generic

from blog.models import *

class IndexView(generic.ListView):
    template_name = 'blog/list2.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(published=True)

class List(generic.ListView):
    template_name = 'blog/tree.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.filter(published=True)

def index(request):
    """Main listing."""
    posts = Post.objects.filter(published=True)
    paginator = Paginator(posts, 2)

    try: page = int(request.GET.get("page", '1'))
    except ValueError: page = 1

    try:
        posts = paginator.page(page)
    except (InvalidPage,EmptyPage):
        posts = paginator.page(paginator.num_pages)

    return render_to_response("blog/tree.html", dict(posts=posts, user=request.user))

class PostView(generic.DetailView):
    model = Post
    template_name = 'blog/post.html'

def post(request, slug):
    post = get_object_or_404(Post,slug=slug)
    return render(request,'blog/post.html',{'post':post})
