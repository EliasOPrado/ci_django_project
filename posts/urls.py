from django.conf.urls import url,
from .views import get_posts, post_detail, create_or_edit_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts')
]
