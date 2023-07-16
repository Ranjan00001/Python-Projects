"""
A module to show simple, input-driven animation.

This is a simple animation where we move an image
according to the pressed keys.
"""
import introcs
import random
import math
from game2d import *
import time

#####CONSTANTS#####
# Window Size
WINDOW_WIDTH = 512
WINDOW_HEIGHT = 512

# AMOUNT TO CHANGE THE POSITION PER FRAME
ANIMATION_STEP = 2

##### CONTROLLER CLASS ######
class Animation(GameApp):
	"""
	This class is an application to animate an image with the arrow keys.

	At each step, the update() method checks for key input
	and moves the image accordingly.

	Attribute view: the view (inherited from GameApp)
	Invariant: view is an instance of GView

	Attribute image: the image to animate
	Invariant: image is a GImage made from a PNG file
	"""

	# THE THREE MAIN METHODS
	def start(self):
		"""
		Initializes the application, creating new attributes.
		"""
		# Image files must be stored in a folder called Image
		self.image = GImage(x=WINDOW_WIDTH/2,y=WINDOW_HEIGHT/2,width=100,height=100,source='Walker.png')
		


	def update(self,dt):
		"""
		Animates the image.

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		# Use if instead of elif to allow multiple keys at once
		if self.input.is_key_down('up'):
			self.image.y += ANIMATION_STEP
		if self.input.is_key_down('down'):
			self.image.y -= ANIMATION_STEP
		if self.input.is_key_down('right'):
			self.image.x += ANIMATION_STEP
		if self.input.is_key_down('left'):
			self.image.x -= ANIMATION_STEP


	def draw(self):
		"""
		Draws the image
		"""
		self.image.draw(self.view)


# APPLICATION CODE
if __name__ == '__main__':
	Animation(left=150,width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()
	

