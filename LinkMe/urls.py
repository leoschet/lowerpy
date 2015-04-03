from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LinkMe.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/login', include(admin.site.urls)),
    # index
    url(r'^$', 'linkme_app.views.index', name='index'),
    # register link
    url(r'^register', 'linkme_app.views.register', name='register'),
    # source link
	url(r'^(?P<source>\w+)', 'linkme_app.views.redirectTo', name='redirect' ),

)
