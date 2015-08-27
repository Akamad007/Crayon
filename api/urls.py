from django.conf.urls.defaults import *


urlpatterns = patterns('api.views',
    # Examples:
    url(r'^add/$', 'getFavicon'), 
 
    url(r'^all/$', 'uploadFile'),
    
)