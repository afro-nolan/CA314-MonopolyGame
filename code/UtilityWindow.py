import pyglet
from pyglet.window import key

class UtilityWindow(pyglet.window.Window):

	def __init__(self, game, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.game = game #game
		pyglet.gl.glClearColor(0.3,0.4,0.5, 1) #Background colour
		self.set_location(100, 100) #Set the location of the window
		self.labels = []
		#Title Label
		self.title_label = pyglet.text.Label('You landed on an Utility',
                         font_name='Times New Roman',
                         font_size=70,
                         x=self.width//2, y=self.height - 100,
                          anchor_x='center', anchor_y='center', color=(0, 0, 0, 255))
		self.labels.append(self.title_label)


	def on_draw(self):
		"""Draws on the screen"""
		self.render()

	def render(self):
		"""Renders the screen"""
		#Clear screen
		self.clear()
		#Draw labels
		for l in self.labels:
			l.draw()

	def exit_callback(self, t):
		"""Exit the window"""
		self.close()

	def on_key_press(self, symbol, modifier):
		if symbol == key.ENTER or symbol == key.RETURN:
			from gameboardstarterwindow import startgamewindow
			pyglet.clock.schedule_once(self.exit_callback , 2)
			startgamewindow(self.game)
