from django.urls import path
from .views import PostListAPIView, PostCreateAPIView,PostDetailAPIView,PostDeleteAPIView,PostUpdateAPIView
app_name = 'api'
urlpatterns = [
    path('', PostListAPIView.as_view(), name='api_list'),
    path('create/', PostCreateAPIView.as_view(), name='api_create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='api-detail'),
    path('<int:pk>/delete', PostDeleteAPIView.as_view(), name='api-delete'),
    path('<int:pk>/update', PostUpdateAPIView.as_view(), name='api-update'),

]