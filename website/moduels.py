from flask import Blueprint, render_template, request, redirect, url_for
from . import db
from datetime import datetime


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(300), unique = True)
    complete= db.Column(db.Boolean, default= False)
    date= db.Column(db.DateTime, default= datetime.now)

#!line1-4: I've imported all of the moduels and classes that I'm using 

#!line6: I've acccessed the class ToDo and then accessed it's variables that are inside the brackets.

#*line7-10: I've created 4 seperate variables which all have their own assignment operator and all used the function column so that it'll create 4 seperate columns onto my database. the differences are that I've used an integer function so that in my database it will filter out the coloumns with numbers to create an order of 1,2,3 etc. then used a boolean of true
#*for the second column i've used a string funcion so that i am able to type out what is on my to do list use characters that have a maximum of 300 chracters. then used a boolean of true.
#* For the third column I've used the boolean function so that if the default equals false it will print 0 for incomplete because it's been eqauled to FALSE.
#* For the forth column I've used a date time function  and then created a function called default and then accessed the class using datetime and then used a dot notation of .now so that in my database it'll so the exact date of when then task was added to the database.

#! for classes and imports
#* for the variables and functions 