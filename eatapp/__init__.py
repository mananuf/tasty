from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
# from flask_login import LoginManager
from flask_uploads import IMAGES, UploadSet, configure_uploads, patch_request_class
import os

basedir = os.path.abspath(os.path.dirname(__file__))    # sets path to save image files
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///eatapp.db'   # DB configuration
app.config['SECRET_KEY'] = '3708e7eeb081d7d5823ba3388e15f1a34a9e1b4c91e417669a710e787d0aa4d5'
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(basedir, 'static/img')    # indicates directory where files will be saved to

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)  # loads configuration for upload sets
patch_request_class(app)    # limits size of file to 16MB


db = SQLAlchemy(app)    # instantiating SQLalchemy
bcrypt = Bcrypt(app)    # Bcrpt instance
# login_manager = LoginManager(app)


from eatapp import routes   # display routes
from eatapp.foods import routes #display routes