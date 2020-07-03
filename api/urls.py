from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet


urlpatterns = []

router = DefaultRouter()
router.register(r'post', PostViewSet, 'post')
urlpatterns += router.urls
