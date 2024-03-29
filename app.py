from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db,Pet
from forms import AddPetForm, EditPetForm

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] =False

toolbar= DebugToolbarExtension(app)

connect_db(app)
db.create_all()

@app.route('/')
def show_home_page():
    """showing home page"""
    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    form = AddPetForm()

    if form.validate_on_submit():
        pet_name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age =form.age.data
        notes = form.notes.data

        new_p= Pet(name = pet_name, species=species, photo_url=photo_url, age=age, notes=notes)
        db.session.add(new_p)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)
    
@app.route('/<int:pet_id>', methods=["GET", "POST"])
def show_pet_details(pet_id):
    """show infomation about the pet and the form to edit info"""
    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.available = form.available.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template('pet_profile.html', pet=pet, form=form)