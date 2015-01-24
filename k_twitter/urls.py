from django.conf.urls import patterns, include, url
#you can uncomment tne next two line to enable the admin

#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'k_twitter.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'k_twitter_app.views.index'),
    url(r'^login$', 'k_twitter_app.views.login_view'),
    url(r'^logout$', 'k_twitter_app.views.logout_view'),
    url(r'^signup$', 'k_twitter_app.views.signup'),
    url(r'^k_twitters$', 'k_twitter_app.views.public'),
    url(r'^submit$', 'k_twitter_app.views.submit'),
    url(r'^users/$', 'k_twitter_app.views.users'),
    url(r'^users/(?P<username>\w{0,30})/$', 'k_twitter_app.views.users'),
    url(r'^follow$', 'k_twitter_app.views.follow'),
)
