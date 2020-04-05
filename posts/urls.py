from django.conf.urls import url
from .views import get_posts, post_detail, create_or_edit_post

"""
All these urls will be included into the main url.py file as post/
-- These urls are based in all the funtions in posts.views. --
"""

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_or_edit_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit_post, name='edit_post'),

]
