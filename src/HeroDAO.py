"""HeroDAO.

Followed the pattern from here: https://flask-restx.readthedocs.io/en/latest/example.html # noqa E501

DAO = Data Access Object
"""
import uuid
import json

DATA_JSON_PATH = "src/data/heros.json"


class HeroDAO(object):
    """HeroDAO."""

    def __init__(self):
        self.heros = self.load_from_json()

    def load_from_json(self):
        """Load data from json."""
        heros = []
        with open(DATA_JSON_PATH, "r") as f:
            heros = json.loads(f.read())
        return heros

    def save_to_json(self):
        """Write Data to json."""
        with open(DATA_JSON_PATH, "w") as f:
            f.write(json.dumps(self.heros))

    def get(self, id, api):
        """Get Hero(s)."""
        for hero in self.heros:
            if hero['id'] == id:
                return hero

        api.abort(404, "Hero {} doesn't exist".format(id))

    def create(self, data):
        """Create Hero."""
        hero = data
        hero['id'] = str(uuid.uuid4())
        self.heros.append(hero)
        self.save_to_json()
        return hero

    def update(self, id, data, api):
        """Update Hero."""
        hero = self.get(id, api)
        hero.update(data)
        self.save_to_json()
        return hero

    def delete(self, id, api):
        """Delete Hero."""
        hero = self.get(id, api)
        self.heros.remove(hero)
        self.save_to_json()
