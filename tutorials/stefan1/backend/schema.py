import graphene
from graphene import relay, ObjectType, List, Field, String, Int


persons = [
    {'id': '1', 'first_name': 'Isaac', 'last_name': 'Newton'},
    {'id': '2', 'first_name': 'Alonzo', 'last_name': 'Church'},
    {'id': '3', 'first_name': 'Haskell', 'last_name': 'Curry'},
    {'id': '4', 'first_name': 'Alan', 'last_name': 'Turing'},
    {'id': '5', 'first_name': 'Edwin Thompson', 'last_name': 'Jaynes'}
]


def get_person(person_id):
    for p in persons:
        if p['id'] == person_id:
            return p
    raise ValueError(':/')


class Person(ObjectType):
    class Meta:
        interfaces = (relay.Node, )

    first_name = String(required=True)
    last_name = String(required=True)

    @staticmethod
    def get_node(cls, info, id):
        return get_person(id)


class Query(ObjectType):
    node = relay.Node.Field()

    hello = Field(String, name=String(default_value='stranger'))

    newton = Field(Person)

    def resolve_newton(parent, info):
        return get_person('1')

    def resolve_hello(parent, info, name):
        return f'Hello {name}!'



    # persons = Field(List(Person), n=Int(default_value=1, required=True))

    # def resolve_persons(parent, info, n):
    #     return dudes[:n]
schema = graphene.Schema(query=Query)
