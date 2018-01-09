from django.urls import path
from . import views
from django.conf.urls import url


urlpatterns = [
    path('', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    # path('')
]
