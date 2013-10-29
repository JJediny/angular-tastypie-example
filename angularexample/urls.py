from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.conf import settings

from tastypie.api import Api
from angularexample.todo.resources import TodoResource

v1_api = Api(api_name='v1')
v1_api.register(TodoResource())


urlpatterns = patterns('',

    url(
        regex = r'^$',
        view = TemplateView.as_view(template_name = 'todo.html'),
        name = 'homepage'
    ),

    url(r'^api/', include(v1_api.urls)),

    # STATIC AND MEDIA CONTENT
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

)
