from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('', include('posts.urls', namespace='posts')),
    # Add other app URLs as needed
]
