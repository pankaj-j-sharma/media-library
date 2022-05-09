from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(MediaCategory)
admin.site.register(MediaType)
admin.site.register(MediaItem)
