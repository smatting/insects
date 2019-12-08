from flask import Flask
from schema import schema

from flask_graphql import GraphQLView
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

example_query = """
{
  persons(n: 30) {
    firstName
  }
}
"""


app.add_url_rule(
    "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


@app.teardown_appcontext
def shutdown_session(exception=None):
    pass


if __name__ == "__main__":
    print('============================================================')
    print(schema)
    print('============================================================')
    app.run(debug=True)
