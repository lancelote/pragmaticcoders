# pylint: disable=invalid-name

from django.conf.urls import url
from . import views

# ToDo : Allowed category / person chars?
urlpatterns = [
    url(r'event/$', views.post_event),
    url(r'category/(?P<category>[\w-]+)/$', views.last_10_by_category),
    url(r'person/(?P<person>[\w-]+)/$', views.last_10_by_person),
    url(r'time/$', views.last_10_by_time)
]
