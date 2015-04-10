from django.conf.urls import patterns, url
from User import views
from django.views.generic import TemplateView


urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'User/index.html')),
    url(r'choose', views.obtainAccess),
    url(r'images', views.images, name='images')

)#views.obtainAccess, name='choose'