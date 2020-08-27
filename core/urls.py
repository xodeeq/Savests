from django.conf import settings
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    # sv001
    path('', admin.site.urls),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]