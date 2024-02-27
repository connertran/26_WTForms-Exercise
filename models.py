"""Models for adopt app."""
from flask_sqlalchemy import SQLAlchemy

default_pet_img= "https://www.eiu.edu/_eiu22/ou/includes/global/profile_image.php?id=ajoshi&ts=1704267585"

db = SQLAlchemy()
def connect_db(app):
    db.app = app
    db.init_app(app)
    app.app_context().push()

# All models go below
class Pet(db.Model):
    """This models a pet potentially available for adoption"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text,
                          nullable = True)
    age = db.Column(db.Integer,
                    nullable=True)
    notes= db.Column(db.Text,
                     nullable=True)
    available=db.Column(db.Boolean,
                        nullable=False,
                        default=True)
    def image_url(self):
        """Return image for pet -- bespoke or generic."""

        return self.photo_url or default_pet_img