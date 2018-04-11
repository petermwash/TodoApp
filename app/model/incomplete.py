import random

from .todo import Todo

class Incomplete(Todo):
	def __init__(self, activity):
		id = random.randint(1, 500)
		super(Incomplete, self).__init__(id, activity, done=False)

	def __repr__(self):
		return '<Incomplete()>'