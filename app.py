from flask import Flask, jsonify, request
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from config import Config
from models import Hero, Power, HeroPower, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///superheroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db = SQLAlchemy(app)
migrate = Migrate(app, db)

db.init_app(app)
# Retries all the heroes.
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]), 200

#delete a hero from the database.
@app.route('/heroes/<int:id>', methods=['DELETE'])
def delete_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    db.session.delete(hero)
    db.session.commit()
    return jsonify({"message": "Hero deleted"}), 200

#gets a specific hero by their id and if it fails it returns a 404 error .
@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "hero_powers": [{
            "id": hp.id,
            "strength": hp.strength,
            "power": {
                "id": hp.power.id,
                "name": hp.power.name,
                "description": hp.power.description
            }
        } for hp in hero.hero_powers]
    }), 200

#retrieve the power status
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers]), 200

#retrieves a specific power by the id.
@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404
    return jsonify({"id": power.id, "name": power.name, "description": power.description}), 200

#Handles a patch request to the /power/int:id endpoint to update the description of a specific power in the database.
@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if not power:
        return jsonify({"error": "Power not found"}), 404

    data = request.json
    description = data.get('description')
    if description:
        power.description = description
        db.session.commit()
        return jsonify({"id": power.id, "name": power.name, "description": power.description}), 200

    return jsonify({"errors": ["validation errors"]}), 400

# Creates a new relationship between a hero and a power in the database.
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.json

    # Validate required fields
    if not all(key in data for key in ['strength', 'power_id', 'hero_id']):
        return jsonify({"errors": ["Missing fields"]}), 400

    # Create new HeroPower
    try:
        hero_power = HeroPower(
            strength=data['strength'],
            power_id=data['power_id'],
            hero_id=data['hero_id']
        )
        db.session.add(hero_power)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

    return jsonify({
        "id": hero_power.id,
        "hero_id": hero_power.hero_id,
        "power_id": hero_power.power_id,
        "strength": hero_power.strength,
        "hero": {
            "id": hero_power.hero.id,
            "name": hero_power.hero.name,
            "super_name": hero_power.hero.super_name
        },
        "power": {
            "id": hero_power.power.id,
            "name": hero_power.power.name,
            "description": hero_power.power.description
        }
    }), 201

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
