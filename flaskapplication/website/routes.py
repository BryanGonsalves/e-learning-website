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
    if(len(data) <5):
        # opening the json file 
        f = open('courses.json')

        #load json as dictionary
        courses = json.load(f)
        #add course to database
        for course in courses:
            new_course = Course(title=course['title'],author = course['author'],overview = course['overview'],image = course['img'],url = course['url'])
            #adding course to database
            db.session.add(new_course)
            db.session.commit()
        f.close()
    return "Data Loaded Succesfully"




        
