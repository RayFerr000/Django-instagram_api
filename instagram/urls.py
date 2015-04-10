from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = patterns('',url(r'^User/', include('User.urls')),
	url(r'^Home/',TemplateView.as_view(template_name='Home.html')),
	                     
    # Examples:
    # url(r'^$', 'instagram.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
