from django.conf.urls import patterns, include, url
from settings import ROOT

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'blog/', include('blog.urls')),
)
