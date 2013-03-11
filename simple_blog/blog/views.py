from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404

from blog.models import *

def index(request):
    posts = Post.objects.all().order_by('-pub_date')[:5]
    comments = []
    for p in posts:
        l = len(Comment.objects.filter(post=p))
        comments.append(l)
    list = zip(posts, comments)
    return render(request, 'blog/index.html', {'list':list})
    
def post(request, index):
    p = get_object_or_404(Post, pk=index)
    comments = Comment.objects.filter(post=p)
    return render(request, 'blog/post.html', {'post':p, 'comments':comments})

    
def comment_add(request, post):
    raise Http404    

