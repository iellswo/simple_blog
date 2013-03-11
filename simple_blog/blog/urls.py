from django.conf.urls import patterns, include, url
from simple_blog.settings import ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),                  
    url(r'^post/(?P<index>\d+)/$', 'post'),
    url(r'^post/(?P<post>\d+)/comment/(?P<index>\d+)/$', 'comment'),
    url(r'^post/(?P<post>\d+)/comment/add/$', 'comment_add'),
    )
    
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$',
         'django.views.static.serve',
        {'document_root': ROOT('simple_blog/blog/static')}),
)
