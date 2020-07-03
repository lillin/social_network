from django.shortcuts import get_object_or_404

from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from api.models import Post
from api.serializers import PostSerializer
from api.permissions import EditDeleteOnlyOwner

# sign up
# create user view

# sign in
# check if user exists if yes -> 200, then get token


class PostViewSet(ModelViewSet):
    """
    Provides full management of existing posts depending on user permissions.
    """
    permission_classes = (IsAuthenticatedOrReadOnly, EditDeleteOnlyOwner, )
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

    @action(methods=['POST'])
    def like(self):
        # TODO: move like here
        pass


# like post
# unlike post

# like analytics per day (with filter by chosen dates range as url params)
# user activity: last login + last request

# TODO: permission (delete/edit only owner)
#  add registration email,
