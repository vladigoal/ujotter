from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import IndexView

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS[0]}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
