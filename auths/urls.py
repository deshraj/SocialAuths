from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'auths.views.home', name='home'),
    url(r'testaclass', 'auths.views.testaclass', name='testaclass'),
    url(r'trainclass', 'auths.views.trainModel', name='trainModel'),
    url(r'deleteimage', 'auths.views.deleteImage', name='deleteImage'),
    url(r'dashboard', 'auths.views.dashboard', name='dashboard'),
    url(r'material', 'auths.views.material', name='material'),
    url(r'temp', 'auths.views.temp', name='temp'),    
    # url(r'^blog/', include('blog.urls')),
)
