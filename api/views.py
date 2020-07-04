from django.db.models import Count
from django.db.models.functions import TruncDay

from rest_framework.decorators import action
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)
from django_filters import rest_framework as filters

from api.models import (
    Post,
    Like
)
from api.permissions import ModifyOnlyOwner
from api.serializers import (
    SignUpSerializer,
    PostSerializer,
    LikeAnalyticsSerializer
)


class SignUpView(CreateAPIView):
    serializer_class = SignUpSerializer


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
    def like(self):
        post = self.get_object()
        # TODO: remove to separate method in Post obj.
        # make it through get or create
        like = Like.objects.filter(user=self.request.user, post=post)
        if like.exists():
            like.delete()
            like = False
            post.likes_amount -= 1
        else:
            Like.objects.create(user=self.request.user, post=post)
            like = True
            post.likes_amount += 1
        post.save(update_fields=['likes_amount', ])
        return Response({"like": like})


class LikeAnalyticsView(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeAnalyticsSerializer
    filter_backends = (filters.DjangoFilterBackend,)

    def get_queryset(self):
        queryset = \
            Like.objects.annotate(date=TruncDay('created_at')).values('date').annotate(amount=Count('id'))
        return queryset


# TODO: user activity: last login + last request
