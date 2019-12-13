import graphene

import insects_backend.insects.schema


class Query(insects_backend.insects.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

schema = graphene.Schema(query=Query)


# if __name__ == "__main__":
#     ## Save schema
#     with open('schema.graphql', 'w'):
#         f.write(str(schema))
