from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from api.views import (
    SignUpView,
    SignInView,
    PostViewSet,
    LikeAnalyticsView,
    UserActivityView
)

urlpatterns = [
    path('sign_up/', SignUpView.as_view()),
    path('sign_in/', SignInView.as_view()),

    path('analytics/', LikeAnalyticsView.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

router = DefaultRouter()
router.register(r'post', PostViewSet, 'post')
router.register(f'user_activity', UserActivityView, 'user_activity')
urlpatterns += router.urls
