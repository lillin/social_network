import graphene

from api.models import Post
from api.object_types import PostType


class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.String())

    def resolve_posts(root, info, **kwargs):
        return Post.objects.all()

    def resolve_post_by_id(root, info, id):
        return Post.objects.get(pk=id)
