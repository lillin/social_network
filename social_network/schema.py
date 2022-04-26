import graphene

from api.queries import Query

# GraphQL Schema with defined object types

schema = graphene.Schema(query=Query)
