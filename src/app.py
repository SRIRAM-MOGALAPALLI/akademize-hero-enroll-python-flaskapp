"""Flask Restful App.

Followed the pattern from here: https://flask-restx.readthedocs.io/en/latest/example.html # noqa E501
"""
from flask import Flask
from flask_restx import Api, Resource, fields
from werkzeug.middleware.proxy_fix import ProxyFix
from HeroDAO import HeroDAO
app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app,
    version="1.0",
    title="Hero Enroll Service",
    description="Super Hero Enroll Service for world peace.",
    doc="/",
    validate=True,
)
ns = api.namespace('heros', description='Hero operations')
DAO = HeroDAO()

hero_model = api.model('Hero', {
    'id': fields.String(readonly=True, description='The hero unique identifier'),
    'name': fields.String(required=True, description='The hero name'),
    'alter_ego': fields.String(required=True, description='The hero alter ego')
})


@ns.route('/')
class HeroList(Resource):
    """Shows a list of all heros.

    And lets you POST to add new heros.
    """

    @ns.doc('list_heros')
    @ns.marshal_list_with(hero_model)
    def get(self):
        """List all Heros."""
        return DAO.heros

    @ns.doc('create_hero')
    @ns.expect(hero_model)
    @ns.marshal_with(hero_model, code=201)
    def post(self):
        """Create a new hero."""
        return DAO.create(api.payload), 201


@ns.route('/<string:id>')
@ns.response(404, 'Hero not found')
@ns.param('id', 'The hero identifier')
class Hero(Resource):
    """Show a single hero.

    And lets you delete them.
    """

    @ns.doc('get_hero')
    @ns.marshal_with(hero_model)
    def get(self, id):
        """Fetch a given resource."""
        return DAO.get(id, api)

    @ns.doc('delete_hero')
    @ns.response(204, 'Hero deleted')
    def delete(self, id):
        """Delete a task given its identifier."""
        DAO.delete(id, api)
        return '', 204

    @ns.expect(hero_model)
    @ns.marshal_with(hero_model)
    def put(self, id):
        """Update a task given its identifier."""
        return DAO.update(id, api.payload, api)
