from django.urls import path
from . import views
from django.conf.urls import url

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    # url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail, name='post_detail'),
    # path('', views.PostListView.as_view(), name='post_list'),  # When using generic views
    url(r'^(?P<post_id>\d+)/share/$', views.post_share, name='post_share'),
]
