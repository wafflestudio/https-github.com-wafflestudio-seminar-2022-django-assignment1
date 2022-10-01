from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from blog import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet, basename='post')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v2/posts/', views.post_list),
    path('v2/posts/<int:pk>', views.post_detail),
]
