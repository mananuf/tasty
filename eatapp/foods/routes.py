from flask import session,redirect,render_template,request,flash,url_for, current_app
from eatapp import app, db, photos
from eatapp.foods.models import Categories, Food
from eatapp.foods.forms import AddFood
import secrets, os  # secrets to hash image name / os to find file path



#----------------------- ADMIN ROUTE  ---------------------------------
@app.route("/admin")
def admin():
    return render_template('admin/admin.html')


#----------------------- CATEGORY ROUTE  ---------------------------------
@app.route("/category")
def category():
    categories = Categories.query.all()
    

    # DELETING ITEMS FROM CATEGORY TABLE
    if request.method == "POST":
        pass
    return render_template('admin/category.html', title='Category', categories=categories)



#----------------------- UPDATE CATEGORY ROUTE  ---------------------------------
@app.route("/updatecategory/<int:id>" , methods=['GET','POST'])
def updateCategory(id):
    update_category = Categories.query.get_or_404(id)   # get data in Categories model class with the specified id
    category = request.form.get('update-category')     # get data from update route

    if request.method == 'POST':
        update_category.category_name = category    # from specied id, get category name and change with newly inputted vlaue 
        flash(f'{update_category.category_name} was successfully modified', 'success')
        db.session.commit()     # save changes to database
        
        return redirect(url_for('category'))    # redirect to category page

    return render_template('admin/updatecategory.html', title="update brand", update_category=update_category)




#----------------------- FOOD ROUTE  ---------------------------------
@app.route("/foods")
def foods():
    foods = Food.query.all()
    return render_template('admin/foods.html', title='Foods', foods=foods)


#----------------------- UPDATE CATEGORY ROUTE  ---------------------------------
@app.route("/updatefood/<int:id>", methods=["GET","POST"])
def updateFood(id):
    categories = Categories.query.all()     # get all data from Categories table
    update_food = Food.query.get_or_404(id)     # get specific item id
    form = AddFood(request.form)                # AddFood form instance
    category = request.form.get('category')     #get category from form

    # get form data
    if request.method == 'POST':
        update_food.food_name = form.food_name.data
        update_food.price = form.price.data
        update_food.discount = form.discount.data
        update_food.stock = form.stock.data
        update_food.description = form.description.data
        update_food.category_id = category

        # ---------------- DELETING AND UPLOADING NEW IMAGE
        if request.files.get('image'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/img/" + update_food.image))   # get image from path and delete
                update_food.image = photos.save(request.files.get('image'), name=secrets.token_hex(7) + '.')    # get the image and save with a hashed name
            except:
                update_food.image = photos.save(request.files.get('image'), name=secrets.token_hex(7) + '.')
        
        db.session.commit() # save changes

        flash(f"modifications have been successfully made!","success")

        return redirect(url_for('foods'))

    form.food_name.data = update_food.food_name     # update food name
    form.price.data  = update_food.price   # update price
    form.discount.data = update_food.discount    # update discount
    form.stock.data = update_food.stock     # update stock
    form.description.data  =update_food.description     # update description

    

    return render_template('admin/updatefood.html', title="Update Food", form=form, categories=categories, update_food=update_food)




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
        
        return redirect(url_for('category'))

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