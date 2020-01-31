import graphene

# import insects_backend.insects.schema

from insects_backend.insects.schema import Query, Mutations


schema = graphene.Schema(query=Query, mutation=Mutations)
