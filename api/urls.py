from django.urls import path
from .views import PostListAPIView, PostCreateAPIView,PostDetailAPIView,PostDeleteAPIView,PostUpdateAPIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'api'
urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', PostListAPIView.as_view(), name='api_list'),
    path('create/', PostCreateAPIView.as_view(), name='api_create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='api-detail'),
    path('<int:pk>/delete', PostDeleteAPIView.as_view(), name='api-delete'),
    path('<int:pk>/update', PostUpdateAPIView.as_view(), name='api-update'),

]