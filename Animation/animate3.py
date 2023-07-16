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
	# Attribute _animator: A coroutine for performing an animation
	# Invariant: _animator is a generator-based coroutine

	
	# THE THREE MAIN METHODS
	def start(self):
		"""
		Initializes the application, creating new attributes.
		"""
		# Image files must be stored in a folder called Image
		self.image = GImage(x=WINDOW_WIDTH/2,y=WINDOW_HEIGHT/2,width=100,height=100,source='Walker.png')
		self.image.angle = 0
		self._animator = None
		

	def update(self,dt):
		"""
		Animates the image.

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		if not self._animator is None:
			try:
				self._animator.send(dt)
			except:
				self._animator = None
		elif self.input.is_key_down('left'):
			self._animator = self._animate_turn('left')
			next(self._animator)
		elif self.input.is_key_down('right'):
			self._animator = self._animate_turn('right')
			next(self._animator)
		elif self.input.is_key_down('up'):
			self._animator = self._animate_slide('up')
			next(self._animator)
		elif self._input.is_key_down('down'):
			self._animator = self._animate_slide('down')
			next(self._animator)


	def draw(self):
		"""
		Draws the image
		"""
		self.image.draw(self.view)


	def _animate_turn(self,direction):
		"""Animates a rotation of the image over SPEED seconds
		This method rotates the image from self._sangle to self._fangle

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		
		Parameter direction: The direction to rotate
		Precondition: direction is a string and one of 'left', 'right', 'up' and 'down'
		"""
		sangle = self.image.angle
		if direction == 'left':
			fangle = sangle + 90
		else:
			fangle = sangle - 90

		# Compute degrees per second
		steps = (fangle-sangle)/ANIMATION_STEP
		animating = True
		
		while animating:
			# get the current time
			dt = (yield)
			amount = steps*dt

			# Update the angle
			self.image.angle = self.image.angle+amount
		
			# If we go too far, clamp and stop animating
			if abs(self.image.angle-sangle) >= 90:
				self.image.angle = fangle
				animating = False


	def _animate_slide(self,direction):
		"""
		Animates a vertical up or down of the image over ANIMATION_SPEED

		This method moves the image from self._svert to self._fvert

		Parameter dt: The time since the last animation frame
		Precondition: dt is a float
		"""
		svert = self.image.y
		if direction == 'up':
			fvert = svert + self.image.height
		else:
			fvert = svert - self.image.height

		# Degrees per second
		steps = (fvert - svert)/ANIMATION_STEP
		animating = True

		while animating:
			# get the current time
			dt = (yield)
			amount = steps*dt

			# Update the position
			self.image.y = self.image.y + amount

			# If we go too far, clamp and stop animating
			if abs(self.image.y - svert) >= self.image.height:
				self.image.y = fvert
				animating = False


# APPLICATION CODE
if __name__ == '__main__':
	Animation(width=WINDOW_WIDTH,height=WINDOW_HEIGHT,fps=60.0).run()