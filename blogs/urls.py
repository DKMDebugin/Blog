# urls module for blogs app

from django.conf.urls import url
from . import views

urlpatterns = [
    # home page
    url(r'^$', views.home, name='home'),
    # new posts
    url(r'^new_post/$', views.new_post, name='new_post'),
    # post
    url(r'^post/(?P<post_id>\d+)/$', views.post, name='post'),
    # edit post
    url(r"^edit_post/(?P<post_id>\d+)/$", views.edit_post, name='edit_post'),
]
