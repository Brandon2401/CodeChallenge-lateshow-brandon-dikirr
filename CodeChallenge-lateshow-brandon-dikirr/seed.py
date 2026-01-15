from app import app
from models import db, Episode, Guest, Appearance

with app.app_context():
    Appearance.query.delete()
    Episode.query.delete()
    Guest.query.delete()

    e1 = Episode(id=1, date="1/11/99", number=1)
    e2 = Episode(id=2, date="1/12/99", number=2)

    g1 = Guest(id=1, name="Michael J. Fox", occupation="actor")
    g2 = Guest(id=2, name="Sandra Bernhard", occupation="Comedian")
    g3 = Guest(id=3, name="Tracey Ullman", occupation="television actress")

    a1 = Appearance(id=1, rating=4, episode_id=1, guest_id=1)

    db.session.add_all([e1, e2, g1, g2, g3, a1])
    db.session.commit()

    print("Database seeded successfully!")
