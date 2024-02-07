from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'api'
urlpatterns = [
    path('', views.PostListAPIView.as_view(), name='api-list'),
    path('<int:pk>/', views.PostDetailAPIView.as_view(), name='api-detail'),
    path('<int:pk>/update', views.PostUpdateAPIView.as_view(), name='api-update'),
    path('<int:pk>/delete', views.PostDeleteAPIView.as_view(), name='api-delete'),
    path('create/', views.PostCreateAPIView.as_view(), name='api-create'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

