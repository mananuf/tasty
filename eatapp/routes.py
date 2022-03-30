from flask import redirect, render_template, request, session, url_for, flash

from eatapp import app, db, bcrypt
from eatapp.admin.forms import RegistrationForm, LoginForm
from .models import User
from eatapp.foods.models import Food, Categories



# ------------- home route ----------------------
@app.route('/')
def home():
    page = request.args.get('page',1, type=int) # get pages from page
    foods = Food.query.filter(Food.stock > 0).paginate(page=page, per_page=6)   # get foods that have stock value > 0 (available) 
                                                                                # and paginate items in page
    return render_template("home.html", foods=foods)


# ------------- Register route -------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()   # form instance

    if request.method == 'POST' and form.validate_on_submit():  # if form method is post and details are valid
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')   # get password data and hash/encrypt
        
        user = User(username=form.username.data, email = form.email.data, password=hashed_password)     # get data & put into DB datafields
        db.session.add(user)    # add to DB
        db.session.commit()     # save changes to DB

        flash(f'Welcome {form.username.data}! Your registration was successful!', category='success')   # display this, if all conditions are met

        return redirect(url_for('login'))   # redirect to login page
    return render_template('register.html', title='registration', form=form)



# ------------- Login route -------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()   # form instance for login

    if request.method == 'POST' and form.validate_on_submit():  # if form method is post and details are valid
        
        
        user = User.query.filter_by(email = form.email.data).first()     # get the first result that matches input
        
        if user and bcrypt.check_password_hash(user.password, form.password.data):  # check if inputted password matches one in DB
            session['email'] = form.email.data
            next_page = request.args.get('next')

            flash(f'Login successful! Continue shopping', category='success')   # display this, if all conditions are met

            return redirect(next_page or url_for('home'))  # redirect to next page if it exists, or go to home

        else:   # if details do not match one in DB
            flash('Login unsuccessful! Please enter email and password correctly', 'danger')
    return render_template('login.html', title='login', form=form)
