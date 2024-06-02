from app import create_app
from app.controllers import index, add, tasks

app = create_app()

@app.route('/')
def index_route():
    return index()

@app.route('/add', methods=['POST'])
def add_route():
    return add()

@app.route('/tasks')
def tasks_route():
    return tasks()

if __name__ == '__main__':
    app.run(debug=True)