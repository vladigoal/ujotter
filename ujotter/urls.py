from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import main_view, login_view

urlpatterns = patterns('',
    (r'^$', main_view),
    (r'login.html', login_view),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
