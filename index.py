from flask import Flask, render_template, redirect, url_for, request

from app.model.todo import Todo
from app.model.incomplete import Incomplete

app = Flask(__name__)

todos = [
Incomplete('Work on project')
]

@app.route('/')
def index():
	incomplete = filter(lambda t: t.done == False, todos)
	complete = filter(lambda t: t.done == True, todos)

	return render_template('index.html', complete=complete, 
		incomplete=incomplete)

@app.route('/add', methods = ['POST'])
def add():
	if (request.method == 'POST'):
		todo = Incomplete(activity = request.form['todo_item'])
		todos.append(todo)

		return redirect(url_for('index'))

@app.route('/done/<int:id>')
def done(id):
	for todo in todos:
		if todo.id == id:
			todo.done = True

	return redirect(url_for('index'))

@app.route('/remove/<int:id>')
def remove(id):
	for todo in todos:
		if todo.id == id:
			todos.remove(todo)

	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(debug=True)