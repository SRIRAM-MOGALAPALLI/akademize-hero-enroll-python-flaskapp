"""Flask Restful App.

Followed the detail documented tutorial
Updated at May 07, 2020
https://rahmanfadhil.com/flask-rest-api/
Differences from the tutorial:
- Flask0restx instead of flat-restful
- Hero Object instead of (Blog)Post
"""
from flask import Flask, request
from flask_restx import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heros.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(
    app,
    version="1.0",
    title="Hero Enroll Service",
    description="Super Hero Enroll Service for world peace.",
    doc="/",
    validate=True,
)


class Hero(db.Model):
    """Hero Class."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    alter_ego = db.Column(db.String(50))

    def __repr__(self):
        """Represent the Object in String format."""
        return '<Post %s>' % self.name


class HeroSchema(ma.Schema):
    """Hero Schema Class."""

    class Meta:
        """Express the Schema Meta object."""

        fields = ("id", "name", "alter_ego")
        model = Hero


hero_schema = HeroSchema()
heros_schema = HeroSchema(many=True)


class HeroListResource(Resource):
    """HeroListResource."""

    def get(self):
        """Get all available heros."""
        posts = Hero.query.all()
        return heros_schema.dump(posts)

    # TODO: Annotate this to get the param schema in swagger ui
    # Find the right config to use marshmallow schema HeroSchema
    def post(self):
        """Create a new hero."""
        new_hero = Hero(
            name=request.json['name'],
            alter_ego=request.json['alter_ego']
        )
        db.session.add(new_hero)
        db.session.commit()
        return hero_schema.dump(new_hero)


class HeroResource(Resource):
    """Hero Resource Class."""

    def get(self, hero_id):
        """Get Hero With ID."""
        hero = Hero.query.get_or_404(hero_id)
        return hero_schema.dump(hero)

    def patch(self, hero_id):
        """Update a Hero."""
        hero = Hero.query.get_or_404(hero_id)

        if 'name' in request.json:
            hero.name = request.json['name']
        if 'content' in request.json:
            hero.alter_ego = request.json['alter_ego']

        db.session.commit()
        return hero_schema.dump(hero)

    def delete(self, hero_id):
        """Delete a hero."""
        hero = Hero.query.get_or_404(hero_id)
        db.session.delete(hero)
        db.session.commit()
        return '', 204


api.add_resource(HeroListResource, '/heros')
api.add_resource(HeroResource, '/heros/<int:hero_id>')
