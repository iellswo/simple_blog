from django.conf.urls import patterns, include, url
from settings.settings import ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
    url(r'^$', 'index'),                  
    url(r'^post/(?P<index>\d+)/$', 'post'),
    url(r'^post/(?P<post>\d+)/comment/add/$', 'comment_add'),
    )
    
urlpatterns += patterns('',
    url(r'^static/(?P<path>.*)$',
         'django.views.static.serve',
        {'document_root': ROOT('blog_master/blog/static')}),
)
