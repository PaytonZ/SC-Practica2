from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views 
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mashupSCdjango.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^insertdata$', views.process_data),
    url(r'^facebooktest', views.facebook_login),
    url(r'^getdata', views.obtain_data),
    url(r'^shorturl', views.short_url),
    url(r'^$', views.main),
)
