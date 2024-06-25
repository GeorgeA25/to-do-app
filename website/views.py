from flask import Blueprint, render_template, request, redirect, url_for
from .moduels import Todo
from . import db

my_view= Blueprint("my_view", __name__)

@my_view.route("/")
def home():
    todo_list= Todo.query.all()
    message=request.args.get('message', None)
    return render_template("index.html", todo_list=todo_list, message=message)

@my_view.route("/update/<todo_id>")
def update(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    todo.complete= not todo.complete
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo=Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))

@my_view.route("/add", methods=["POST"])
def add():
    try:
     task = request.form.get("task")
     new_todo = Todo(task=task)
     db.session.add(new_todo)
     db.session.commit()
     return redirect(url_for("my_view.home"))
    except:
        message= ("There was an error adding your task. Please try again")
        return redirect(url_for("my_view.home", message=message))


@my_view.route("/edit/<todo_id>", methods=["POST"])
def edit(todo_id):
     todo=Todo.query.filter_by(id=todo_id).first()
     new_title=request.form.get("edit_task")
     todo.task= new_title
     db.session.commit()
     return redirect(url_for("my_view.home"))


#!lines 1-3: I've imported all of the variables, classes and function that im using from the modules that im using

#*line 5: I've created a new variable called my_view and then assigned it to the Blueprint class with __name__ and __main__ inside the brackets.


#*line9: Retrieve all todo items from the database
     
#~line10: Retrieve 'message' parameter from query string (if any)
     
#*line11: Render the index.html template with todo_list and message
    
#*line15 Find the todo item by its id
       
#*line16 Toggle the 'complete' status of the todo item
       
#*line17: Commit the changes to the database
       
#~line18: Redirect to the home route after updating
    
#*line22: Find the todo item by its id
       
#*line23: Delete the todo item from the database
       
#*line24: Commit the changes to the database
       
#~line25:Redirect to the home route after deleting
    
#*line30: Get the task from the POST form data
              
#*line31: Create a new Todo object with the task
               
#*line32: Add the new todo item to the database session
              
#*line33: Commit the changes to the database
             
#~line34: Redirect to the home route after adding
       
#£line35: If an exception occurs (e.g., error adding task), redirect with a message
       
#*42: Find the todo item by its id
    
#*43: Get the new task title from the POST form data
    
#*44: Update the task of the todo item
      
#~45: Commit the changes to the database
     
#todoline46: Redirect to the home route after editing
   

#!for imports 
#*variables
#~for returns statemnets
#£ for the except statement

##used chatgpt for the additional comments