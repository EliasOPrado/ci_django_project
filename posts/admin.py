from django.contrib import admin

# Register your models here.
from .models import Post

#to show up in the /admin page
admin.site.register(Post)
