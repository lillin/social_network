import graphene

from graphene_django.rest_framework.mutation import SerializerMutation

from api.serializers import PostSerializer
from api.object_types import PostType
from api.models import Post


class PostMutation(SerializerMutation):
    class Meta:
        serializer_class = PostSerializer
        model_operations = ['create', 'update']
        lookup_field = 'id'


# TODO: following types, research doc on each
class CreatePostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        body = graphene.String(required=True)

    post = graphene.Field(PostType)

    def mutate(self, info, title, body):
        return Post.objects.create(title=title, body=body)


class UpdatePostMutation(graphene.Mutation):
    # POST
    # PUT

    # use serializers

    class Arguments:
        # The input arguments for this mutation
        pk = graphene.ID()
        title = graphene.String()
        body = graphene.String()

        # what to do with `like` ability?

    # The class attributes define the response of the mutation:
    # output fields of the Mutation when it is resolved
    post = graphene.Field(PostType)

    # function that will be applied once the mutation is called.
    # This method is just a special resolver that we can change data within
    def mutate(self, info, pk, title, body):
        post = Post.objects.get(pk=pk)

        # Notice we return an instance of this mutation
        return UpdatePostMutation(post=post)


class LikePostMutation(graphene.Mutation):
    class Arguments:
        pk = graphene.ID()

    like = graphene.Boolean()

    def mutate(self, info, pk):
        post = Post.objects.get(pk=pk)
        like = post.like(info.user)
        return like


class Mutation(graphene.Mutation):
    post = PostMutation.Field()

    # create_post = CreatePostMutation.Field()
    # update_post = UpdatePostMutation.Field()

    like_post = LikePostMutation
