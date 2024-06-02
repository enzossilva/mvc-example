from flask import request, redirect, url_for
from app.models import get_tasks, add_task
from app.view import render_index, render_tasks

def index():
    tasks = get_tasks()
    return render_index(tasks)

def add():
    task = request.form['task']
    senha = request.form['senha']
    add_task(task,senha)
    return redirect(url_for('tasks_route'))

def tasks():
    tasks = get_tasks()
    return render_tasks(tasks)