from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config
from flask_bootstrap import Bootstrap 
#blueprint
from .my_blueprint import my_blueprint
from app.productos import productos


#Creacion y configuracion 
app = Flask(__name__)
app.config.from_object(Config)
Bootstrap = Bootstrap(app)


#registro de blueprints
app.register_blueprint(my_blueprint)
app.register_blueprint(productos)

#crear los objetos de SQLAlchemy y migrate
db = SQLAlchemy(app)
migrate = Migrate(app , 
                  db)

from .models import Producto,Cliente,Detalle,Venta




