from django.urls import path
from rest_framework.routers import DefaultRouter

from api.views import (
    SignUpView,
    PostViewSet,
    LikeAnalyticsView
)


urlpatterns = [
    path('sign_up/', SignUpView.as_view()),
    path('analytics/', LikeAnalyticsView.as_view()),
]

router = DefaultRouter()
router.register(r'post', PostViewSet, 'post')
urlpatterns += router.urls
