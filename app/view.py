from flask import render_template

def render_index(tasks):
    return render_template('index.html', tasks=tasks)

def render_tasks(tasks):
    return render_template('tasks.html', tasks=tasks)
