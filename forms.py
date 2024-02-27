from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField,SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, Length

list_of_age= [num for num in range(31)]
choices = [(each_num,each_num) for each_num in list_of_age]

class AddPetForm(FlaskForm):
    """Form for adding pets"""
    name = StringField("Pet name", validators=[InputRequired(message="Name cannot be blank")])
    species = SelectField("Species",choices=[('dog','Dog'),('cat','Cat'),('bird','Bird'), ('porcupine', 'Porcupine')])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = SelectField("Age", choices=choices)
    notes= StringField("Notes",validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for editing pet's info"""
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Notes", validators= [Optional(), Length(min=10)])
    available = BooleanField("Available")