from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render

from blog.models import *

def index(request):
    posts = Post.objects.all().order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts':posts})
    
def post(request, index):
    raise Http404
    
def comment(request, post, index):
    raise Http404
    
def comment_add(request, post):
    raise Http404    

