from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views as auth_views
from .settings import DEBUG
from namubufferiapp import restViews


urlpatterns = []

if DEBUG:
    urlpatterns.append(url(r'^api-auth/', include('rest_framework.urls')))

urlpatterns.extend([
    # Examples:
    # url(r'^$', 'namubufferi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/', include(restViews.router.urls)),
    url(r'^', include('namubufferiapp.urls')),
])
