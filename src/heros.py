"""Hero Service."""
import json


def get_heros():
    """Get Heros."""
    heros = []
    with open("src/data/heros.json", "r") as f:
        heros = json.loads(f.read())
    return {"success": True, "data": heros}


def set_heros(heros):
    """Set Heros."""
    with open("src/data/heros.json", "w") as f:
        f.write(json.dumps(heros))
    return {"success": True, "message": "Heros list updated successfully."}


def get_hero_by_id(id):
    """Get Hero By Id."""
    heros = get_heros()["data"]
    my_hero = None
    for hero in heros:
        if hero["id"] == id:
            my_hero = hero
            break

    if my_hero is None:
        return {
            "success": False,
            "message": f"Hero with id {id} not found in our records.",
        }

    return {
        "success": True,
        "data": my_hero
    }


def update_hero(hero):
    """Update Hero."""
    heros = get_heros()["data"]
    heros = get_heros()["data"]
    my_hero = None
    for h in heros:
        if h["id"] == hero["id"]:
            my_hero = h
            break
    if my_hero is None:
        return {
            "success": False,
            "message": f"Hero with id {id} not found in our records.",
        }

    my_hero["name"] = hero["name"]
    my_hero["alter_ego"] = hero["alter_ego"]
    set_heros(heros)
    return {
        "success": True,
        "data": my_hero
    }
