from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LinkMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # index
    url(r'^$', 'LinkMe.views.index', name='index'),
    # register link
    url(r'^register', 'LinkMe.views.register', name='register' ),
    # source link
    url(r'^([0-9]+)', 'LinkMe.views.redirect', name='redirect' ),
)
