from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/v1/auth/', include("rest_framework.urls")),
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('', include('posts.urls', namespace='posts')),
    path('api/v1/schema', SpectacularAPIView.as_view(), name='schema'),
    path('api/v1/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), name='schema-redoc'),
    path('api/v1/schema/swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger'),

    # Add other app URLs as needed
]
