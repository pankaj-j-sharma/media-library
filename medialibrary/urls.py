from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('user_auth.urls')),
    path('', include('media.urls')),
    path('media/', include('media.urls')),
    path('admin/', admin.site.urls),
]
