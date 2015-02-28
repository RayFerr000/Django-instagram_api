from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',url(r'^User/', include('User.urls')),
    # Examples:
    # url(r'^$', 'instagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
