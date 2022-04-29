import graphene

from api.queries import Query
from api.mutations import Mutation

# GraphQL Schema with defined object types

schema = graphene.Schema(query=Query, mutation=Mutation)
