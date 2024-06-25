from flask import Flask
from flask_sqlalchemy import SQLAlchemy



db=SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///db.sqlite'
    db.init_app(app)

    from .views import my_view
    app.register_blueprint(my_view)

    from .moduels import Todo
    with app.app_context():
        db.create_all()
    return app  

#!line 1: I've imported all class that i needed from the seperate moduels.

#*line 6: I've created a new variable called db and then assigned it to the SQLAlchemy classed using the assignement operator

#~line 8: I've created a def then used the function create_app()

#*line 9: then i created a new variable called app an then assigned it to Flask class and inside the bractes used __name__ variable.

#*line 10: i then used the app variable and then used config method. then put in brackects then database i want to use and assigned it to 'sqlite:///db.sqlite'

#*line 11: then i used the db variable and then used a dot notation init_app to initialize the app which is inside the brackets.

#!line 13: i'e imported my_view variable from .views

#*line 14: then used the app variable wit .register_blueprint(my_view) which defines a my blueprint which is in a seperate file and registers it into app.py

#!line 16: i've imported ToDo from the moduels package.

#~line 17: i've used with app.app_context to create the appliaction context for the Flask App.

#*line 18: i used db.create_all() function which will create all the database tables I have made and defined.

#todoline 19: I then added return app which will return to the flask app instance.

#!for imports
#*for variables
#~ for the def and the with
#todo for the return statement