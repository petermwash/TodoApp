class Todo():
	def __init__(self, id, activity, done):
		self.id = id
		self.activity = activity
		self.done = done

	def __repr__(self):
		return '<Todo()>'