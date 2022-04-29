# TODO: learn, if sep file for Query is needed?

import graphene

from api.models import Post
from api.object_types import PostType


class Query(graphene.ObjectType):
    # if resolver maps to DjangoObjectType, it must return Queryset
    posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.String())

    # Query - root object (graph structure),
    # root object must know about all object types
    # info.context attribute is the HTTPRequest
    def resolve_posts(root, info, **kwargs):
        return Post.objects.select_related('creator').all()

    def resolve_post_by_id(root, info, id):
        return Post.objects.get(pk=id)

# Relay usage
