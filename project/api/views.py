from functools import wraps
from flask import flash, redirect, jsonify, session, url_for, Blueprint, make_response
from project import db
from project.models import Task

api_blueprint = Blueprint('api', __name__)


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('users.login'))
    return wrap


def open_tasks():
    return db.session.query(Task).filter_by(status='1').order_by(Task.due_date.asc())

def closed_tasks():
    return db.session.query(Task).filter_by(status='0').order_by(Task.due_date.asc())


@api_blueprint.route('/api/v1/tasks/')
def api_tasks():
    results = db.session.query(Task).limit(10).offset(0).all()
    json_results = []
    for result in results:
        data = {
            'task_id': result.task_id,
            'task name': result.name,
            'due date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user id': result.user_id
            }
        json_results.append(data)
    with open('record.log','a') as f:
      f.write('\n json_results {} \n jsonify(items=json_results) {} \n make_response(jsonify(items=json_results)) {}'.format(json_results,jsonify(items=json_results),make_response(jsonify(items=json_results))))
    return jsonify(items=json_results)


@api_blueprint.route('/api/v1/tasks/<int:task_id>')
def task(task_id):
    result = db.session.query(Task).filter_by(task_id=task_id).first()
    if result:
        result = {
            'task_id': result.task_id,
            'task name': result.name,
            'due date': str(result.due_date),
            'priority': result.priority,
            'posted date': str(result.posted_date),
            'status': result.status,
            'user id': result.user_id
        }
        code = 200
    else:
        result = {"error": "Element does not exist"}
        code = 404
    return make_response(jsonify(result), code)