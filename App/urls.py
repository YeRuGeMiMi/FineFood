from django.conf.urls import patterns, include, url

urlpatterns = patterns('App.views',
    # Examples:
    # url(r'^$', 'FineFood.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$','index',name='index'),
)