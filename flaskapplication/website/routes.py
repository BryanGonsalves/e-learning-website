import json

from flask import Blueprint, render_template, request

from . import db
from .models import Course

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    courses = Course.query.all()
    return render_template('course_view.html', courses=courses)

@routes.route('/loaddata')
def loaddata():
    data = Course.query.all()
    print(len(data))
    if len(data) < 5:
        with open('courses.json') as f:
            courses = json.load(f)
            for course in courses:
                new_course = Course(
                    title=course['title'],
                    author=course['author'],
                    overview=course['overview'],
                    image=course['img'],
                    url=course['url']
                )
                db.session.add(new_course)
                db.session.commit()
    return "Data Loaded Successfully"

