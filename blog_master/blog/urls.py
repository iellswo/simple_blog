from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('blog.views',
                       url(r'^$', 'index'),
                       
                       url(r'^post/(?P<id>\d+)/$', 
                            'post'),
                            
                       url(r'^post/(?P<post>\d+)/comment/(?P<id>\d+)/$',
                            'comment'),
                            
                       url(r'^post/(?P<post>\d+)/comment/add/$',
                            'comment_add'),
                            
                       url(r'^^static/(?P<path>.*)$',
                        'django.views.static.serve',
                        {'document_root': ROOT('static')}),
                      )
