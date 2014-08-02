from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from .api.views import (
    ExampleView,
    UserDetail,
    UserList,
    UserPostList,
    AuthView,
    PostList,
)

user_urls = patterns(
    '',
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/$',
        UserDetail.as_view(), name='user-detail'),
    url(r'^/(?P<username>[0-9a-zA-Z_-]+)/jobs/$',
        UserPostList.as_view(), name='user-jobs-list'),
    url(r'^$', UserList.as_view(), name='user-list'),
)

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'wotoi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'wotoi.core.views.base', name='some_view'),
    url(r'^kf/', include(admin.site.urls)),

    url(
        r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    ),

    url(r'^api/v1/users', include(user_urls)),

    url(r'^api/v1/example/$', ExampleView.as_view()),

    url(r'^api/v1/auth/$',
        AuthView.as_view(),
        name='authenticate'),

    url(r'^api/v1/jobs/$',
        PostList.as_view(), name='jobs-list'),

)
