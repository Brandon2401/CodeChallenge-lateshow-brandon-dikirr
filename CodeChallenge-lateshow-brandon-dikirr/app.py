from flask import Flask, request, jsonify
from models import db, Episode, Guest, Appearance
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route("/episodes")
def episodes():
    episodes = Episode.query.all()
    return jsonify([
        e.to_dict(only=("id", "date", "number"))
        for e in episodes
    ])

@app.route("/episodes/<int:id>")
def episode_by_id(id):
    episode = Episode.query.get(id)

    if not episode:
        return jsonify({"error": "Episode not found"}), 404

    return jsonify(
        episode.to_dict(
            include={
                "appearances": {
                    "only": ("id", "rating", "episode_id", "guest_id", "guest")
                }
            }
        )
    )
 
@app.route("/guests")
def guests():
    guests = Guest.query.all()
    return jsonify([
        g.to_dict(only=("id", "name", "occupation"))
        for g in guests
    ])

