from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response

from blog.models import *

def index:
    posts = Post.objects.all().order_by('pub_date')[:5]
    return render_to_response('blog/index.html')
