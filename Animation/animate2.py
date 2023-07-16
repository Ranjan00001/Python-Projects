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
	# Attribute _animating: Whether we are in the process of animating
	# Invariant: _animating is a boolean

	# Attribute _rotation: Whether the animation is rotation
	# Invariant: _rotation is a boolean

	# Attribute _sangle: The start angle for animation (in degrees)
	# Invariant: _sangle is a float

	# Attribute _fangle: The final angle for animation (in degrees)
	# Invariant: _fangle is a float

	# Attribute _svert: The start y-coordinate position
	# Invariant: _svert is a float

	# Attribute _fvert: The final y-coordinate position
	# Invariant: _fvert is a float


	# THE THREE MAIN METHODS
	def start(self):
		"""
		Initializes the application, creating new attributes.
		"""
		# Image files must be stored in a folder called Image
		self.image = GImage(x=WINDOW_WIDTH/2,y=WINDOW_HEIGHT/2,width=100,height=100,source='Walker.png')
		self.image.angle = 0
		self._animating = False
		self._rotation = False
		self._sangle = 0
		self._fangle = 0
		self._svert = 0
		self._fvert = 0
		print(self.image.height)

	def update(self,dt):
		"""
		Animates the image.

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		if self._animating:
			if self._rotation:
				self._animate_turn(dt)
			else:
				self._animate_slide(dt)
		elif self.input.is_key_down('left'):
			self._animating = True
			self._rotation = True
			self._sangle = self.image.angle
			self._fangle = self._sangle+90
		elif self.input.is_key_down('right'):
			self._animating = True
			self._rotation = True
			self._sangle = self.image.angle
			self._fangle = self._sangle-90
		elif self.input.is_key_down('up'):
			self._animating = True
			self._rotation = False
			self._svert = self.image.y
			self._fvert = self._svert + self.image.height
			print(self._svert)
			print(self._fvert)
		elif self._input.is_key_down('down'):
			self._animating = True
			self._rotation = False
			self._svert = self.image.y
			self._fvert = self._svert - self.image.height


	def draw(self):
		"""
		Draws the image
		"""
		self.image.draw(self.view)


	def _animate_turn(self,dt):
		"""Animates a rotation of the image over SPEED seconds
		This method rotates the image from self._sangle to self._fangle

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		
		# Compute degrees per second
		steps = (self._fangle-self._sangle)/ANIMATION_STEP
		amount = steps*dt
		
		# Update the angle
		self.image.angle = self.image.angle+amount
		
		# If we go too far, clamp and stop animating
		if abs(self.image.angle-self._sangle) >= 90:
			self.image.angle = self._fangle
			self._animating = False


	def _animate_slide(self,dt):
		"""
		Animates a vertical up or down of the image over ANIMATION_SPEED

		This method moves the image from self._svert to self._fvert

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		# Degrees per second
		steps = (self._fvert - self._svert)/ANIMATION_STEP
		amount = steps*dt

		# Update the position
		self.image.y = self.image.y + amount

		# If we go too far, clamp and stop animating
		if abs(self.image.y - self._svert) >= self.image.height:
			self.image.y = self._fvert
			self._animating = False


# APPLICATION CODE
if __name__ == '__main__':
	Animation(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()