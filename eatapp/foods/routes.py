from flask import session,redirect,render_template,request,flash,url_for
from eatapp import app, db, photos
from eatapp.foods.models import Categories, Food
from eatapp.foods.forms import AddFood
import secrets  # to hash image name



#----------------------- ADMIN ROUTE  ---------------------------------
@app.route("/admin")
def admin():
    return render_template('admin/admin.html')


#----------------------- CATEGORY ROUTE  ---------------------------------
@app.route("/category")
def category():
    categories = Categories.query.all()
    return render_template('admin/category.html', title='Category', categories=categories)


#----------------------- FOOD ROUTE  ---------------------------------
@app.route("/foods")
def foods():
    foods = Food.query.all()
    return render_template('admin/foods.html', title='Foods', foods=foods)


#----------------------- ROUTE FOR ADDING CATEGORIES ---------------------------------
@app.route("/addcategory", methods=['GET','POST'])
def addCategory():
    if request.method == 'POST':    # if method request is POST
        get_category = request.form.get('category')     # get the inputted category
        # get_image = request.form.get('category_image')  # get inputted image
        added_category = Categories(category_name=get_category)  # put data into appropraite table column
        
        db.session.add(added_category)    # add to DB
        flash(f'{get_category} was successfully added to Food Categories', 'success')
        db.session.commit()     # save to DB
        
        return redirect(url_for('add_category'))

    return render_template('admin/addcategory.html', title="Add categories", categories='categories')  # render this template



#----------------------- ROUTE FOR ADDING FOOD ---------------------------------
@app.route("/addfood", methods=['GET','POST'])
def addFood():
    categories = Categories.query.all()     # get all categories
    form = AddFood(request.form)

    if request.method == 'POST':
        food_name = form.food_name.data     # get food name
        price = form.price.data     # get price
        discount = form.discount.data     # get discount
        stock = form.stock.data     # get stock
        description = form.description.data     # get description
        category = request.form.get('category')
        image = photos.save(request.files.get('image'), name=secrets.token_hex(7) + '.')    # get the image and save with a hashed name

        # adding food details to db
        addchow = Food(food_name=food_name, price=price, discount=discount, stock=stock,
                        description=description, image=image, category_id =category)

        db.session.add(addchow)
        flash(f'{food_name} has been added to Foods', 'success')
        db.session.commit()
    return render_template('admin/addfood.html', title="Add food", form=form, categories=categories)  # render this template