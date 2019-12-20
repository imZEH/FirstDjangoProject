import graphene
import todoapp.query
import todoapp.mutation


# Query for getting the data from the server.
class Query(todoapp.query.Query, graphene.ObjectType):
    pass


# Mutation for sending the data to the server.
class Mutation(todoapp.mutation.Mutation, graphene.ObjectType):
    pass


# Create schema
schema = graphene.Schema(query=Query,mutation=Mutation)
