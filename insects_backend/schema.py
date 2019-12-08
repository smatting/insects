import graphene

import insects_backend.insects.schema


class Query(insects_backend.insects.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)
