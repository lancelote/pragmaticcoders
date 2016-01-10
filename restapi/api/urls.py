# pylint: disable=invalid-name

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'event/$', views.post_event),
    url(r'category/(?P<category>[\w-]+)/$', views.last_10_by_category),
]
