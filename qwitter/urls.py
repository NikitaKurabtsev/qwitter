from django.contrib import admin
from django.urls import path, include
from qwitter import settings

urlpatterns = [
    path('', include('qwitter_app.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path(r'^__debug__/', include(debug_toolbar.urls)),
    ]
