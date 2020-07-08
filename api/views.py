from django.contrib.auth import get_user_model
from django.db.models import Count
from django.db.models.functions import TruncDate
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
)
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from rest_framework.response import Response
from rest_framework.viewsets import (
    ModelViewSet,
    ReadOnlyModelViewSet
)
from rest_framework_simplejwt.views import TokenViewBase

from api.filters import DatesRangeFilter
from api.models import (
    Post,
    Like
)
from api.permissions import ModifyOnlyOwner
from api.serializers import (
    SignUpSerializer,
    SignInSerializer,
    PostSerializer,
    LikeAnalyticsSerializer,
    UserActivitySerializer
)

User = get_user_model()


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer


class SignInView(TokenViewBase):
    serializer_class = SignInSerializer


class PostViewSet(ModelViewSet):
    """
    Provides full management of existing posts depending on user permissions.
    """
    permission_classes = (IsAuthenticatedOrReadOnly, ModifyOnlyOwner,)
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    def get_serializer_context(self):
        return {"request": self.request}

    @action(detail=True, methods=['POST'])
    def like(self, request, pk):
        post = self.get_object()
        like = post.like(self.request.user)
        return Response({"like": like})


class LikeAnalyticsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeAnalyticsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = DatesRangeFilter

    def get_queryset(self):
        queryset = \
            Like.objects.annotate(date=TruncDate('created_at')).values('date').annotate(amount=Count('id'))
        return queryset


class UserActivityView(ReadOnlyModelViewSet):
    queryset = User.objects.exclude(is_active=False)
    serializer_class = UserActivitySerializer
