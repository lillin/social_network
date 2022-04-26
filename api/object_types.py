from graphene_django import DjangoObjectType
from django.contrib.auth import get_user_model

from api.models import Post


User = get_user_model()


# think of it as a serializer; possible to add custom fields
class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = '__all__'

    # extra_field = graphene.String()
    #
    # def resolve_extra_field(self, info):
    #     return "hello!


# if FK, related object must be defined independently
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset.filter(is_active=True)
