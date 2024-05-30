import json

from flask import Blueprint, render_template, request

from . import db
from .models import Course

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return "Welcome to First Flask Project!"
@routes.route('/loaddata')
def loaddata(): 
    data = Course.query.all()
    print(len(data))
    if len(data) < 5:
        # Opening JSON file
        f = open('courses.json')

        # Load JSON object as an dictionary
        courses = json.load(f)
        
        # Adding all courses to the database
        for course in courses:
            # Creating a new Course
            new_course = Course(title=course['title'], author=course['author'], overview=course['overview'], image=course['img'], url=course['url'])
            # Adding course to database
            db.session.add(new_course)
            db.session.commit()
        # Closing File
        f.close()
        # Success Message
    return "Data Loaded Successfully"


        
