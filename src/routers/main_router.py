from django.urls import include, path

from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('api/v1/', include('src.routers.api_router')),
    path('api/v1/', include('rest_framework.urls')),
]
