"""
Subcontroller module for Planetoids

This module contains the subcontroller to manage a single level (or wave) in the 
Planetoids game.  Instances of Wave represent a single level, and should correspond
to a JSON file in the Data directory. Whenever you move to a new level, you are 
expected to make a new instance of the class.

The subcontroller Wave manages the ship, the asteroids, and any bullets on screen. These 
are model objects. Their classes are defined in models.py.

Most of your work on this assignment will be in either this module or models.py.
Whether a helper method belongs in this module or models.py is often a complicated
issue.  If you do not know, ask on Ed Discussions and we will answer.

Ranjan Singh
Date 16 may 2023
"""
from game2d import *
from consts import *
from models import *
import random
import datetime


# PRIMARY RULE: Wave can only access attributes in models.py via getters/setters
# Level is NOT allowed to access anything in app.py (Subcontrollers are not permitted
# to access anything in their parent. To see why, take CS 3152)

class Wave(object):
    """
    This class controls a single level or wave of Planetoids.
    
    This subcontroller has a reference to the ship, asteroids, and any bullets on screen.
    It animates all of these by adding the velocity to the position at each step. It
    checks for collisions between bullets and asteroids or asteroids and the ship 
    (asteroids can safely pass through each other). A bullet collision either breaks
    up or removes a asteroid. A ship collision kills the player. 
    
    The player wins once all asteroids are destroyed.  The player loses if they run out
    of lives. When the wave is complete, you should create a NEW instance of Wave 
    (in Planetoids) if you want to make a new wave of asteroids.
    
    If you want to pause the game, tell this controller to draw, but do not update.  See
    subcontrollers.py from Lecture 25 for an example.  This class will be similar to
    than one in many ways.
    
    All attributes of this class are to be hidden. No attribute should be accessed 
    without going through a getter/setter first. However, just because you have an
    attribute does not mean that you have to have a getter for it. For example, the
    Planetoids app probably never needs to access the attribute for the bullets, so 
    there is no need for a getter there. But at a minimum, you need getters indicating
    whether you one or lost the game.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # THE ATTRIBUTES LISTED ARE SUGGESTIONS ONLY AND CAN BE CHANGED AS YOU SEE FIT
    # Attribute _data: The data from the wave JSON, for reloading 
    # Invariant: _data is a dict loaded from a JSON file
    #
    # Attribute _ship: The player ship to control 
    # Invariant: _ship is a Ship object
    #
    # Attribute _asteroids: the asteroids on screen 
    # Invariant: _asteroids is a list of Asteroid, possibly empty
    #
    # Attribute _bullets: the bullets currently on screen 
    # Invariant: _bullets is a list of Bullet, possibly empty
    #
    # Attribute _lives: the number of lives left 
    # Invariant: _lives is an int >= 0
    #
    # Attribute _firerate: the number of frames until the player can fire again 
    # Invariant: _firerate is an int >= 0
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def data(self):
        return self._data

    @property
    def firerate(self):
        return self._firerate
    
    @firerate.setter
    def firerate(self, value):
        self._firerate = value

    @property
    def lives(self):
        return self._lives

    @lives.setter
    def lives(self,value):
        self._lives = value

    
    # INITIALIZER (standard form) TO CREATE SHIP AND ASTEROIDS
    def __init__(self, data):
        self._data = data

        # ship creation
        x, y  = self.data['ship']['position']     # position of ship
        angle = self.data['ship']['angle']        # angle of ship
        self._ship = Ship(x, y, angle)

        # bullet creation
        self._bullets = []                        # starting empty
        self._firerate = 0                        # bullet fire rate initiallising with 0

        # asteroids creation
        self._asteroid = create_asteroid(data['asteroids'])

        # lives
        self.lives = SHIP_LIVES

        # frame count
        self.frame_count = 0

        # sound loading
        self._sound = {'pew':Sound('pew1.wav'),'blast1':Sound('blast1.wav'),
                        'blast2':Sound('blast2.wav')}

 
    # UPDATE METHOD TO MOVE THE SHIP, ASTEROIDS, AND BULLETS
    def update(self, inp):
        
        self.frame_count += 1
        if not self._ship is None:
            self._ship.turn(inp)      # turn according to the given input
            self._ship.impulse(inp)   # changes velocity whenever 'up' key is pressed and moves ship
            self._ship.wrap()         # wrap around dead zone

            # shield activation and inactivation
            if self.frame_count < SHIELD_TIME:
                self.shield_active()
            else:
                self.shield_inactive()

            # movement and wrapping about screen asteroids
            for ast in self._asteroid:
                ast.move()
                ast.wrap()

            # bullet creation
            self.firerate += 1
            if inp.is_key_down('spacebar') and self.firerate>BULLET_RATE:
                pos_vect = self._ship.facing * SHIP_RADIUS + Vector2(self._ship.x, self._ship.y)  # x,y is ship's pos
                self._bullets.append(Bullet(pos_vect.x, pos_vect.y, BULLET_COLOR, self._ship.angle))
                self.firerate = 0
                # sound playing
                self._sound['pew'].play()
                
            # movement of bullet
            self.bullet_move()

            # coliision bw two different objects
            self.collision()

    
    # DRAW METHOD TO DRAW THE SHIP, ASTEROIDS, AND BULLETS
    def draw(self,view):
        """
        Draws the ellipse to the application window (view).

        Parameter: The view window
        Precondition: view is a GView.
        """
        if not self._ship is None:
            self._ship.draw(view)
        for i in self._asteroid:
            i.draw(view)
        for i in self._bullets:
            i.draw(view)
    

    # RESET METHOD FOR CREATING A NEW LIFE
    def is_ship_ended(self):
        return self._ship == None #and self._asteroid == []

    def shield_active(self):
        '''
        '''
        self._ship.source = SHIELD_IMAGE

    def shield_inactive(self):
        '''
        '''
        self._ship.source = SHIP_IMAGE

    # ending wave
    def is_asteroid_ended(self):
        return self._asteroid == []


    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def bullet_move(self):
        '''
        helper method for firing of bullet and deleting bullet which is offscreen
        '''
        i = 0
        while i < len(self._bullets):
            self._bullets[i].fire()           # bullet fire

            # deleting bullet outside DEAD_ZONE
            if GAME_WIDTH + DEAD_ZONE < self._bullets[i].x or self._bullets[i].x < -DEAD_ZONE:
                del self._bullets[i]

            elif GAME_HEIGHT + DEAD_ZONE < self._bullets[i].y or self._bullets[i].y < -DEAD_ZONE:
                del self._bullets[i]

            else:
                i += 1


    def collision(self):
        '''
        removes the object after collision
        '''
        i = 0
        while i < len(self._asteroid):

            # ship and asteroids collision detection
            var = self._ship.is_collided(self._asteroid[i])

            # if asteroid and bullet collide delete both by their respective list
            ast_live = 1                # keep track on asteroid[i]
            size = self._asteroid[i].size
            j = 0
            while j < len(self._bullets):
                if self._bullets[j].is_collided(self._asteroid[i]):
                    del self._asteroid[i]                     # destroy asteroid
                    ast_live = 0
                    # add smaller asteroids broken after collision bw bullet and asteroid
                    self.add_asteroid(self._bullets[j], size)

                    del self._bullets[j]                     # destroy bullet
                    # sound playing
                    self._sound['blast2'].play()
                    break
                j += 1

            # ship and asteroid collision resolution
            if var:
                if ast_live == 1:
                    del self._asteroid[i]
                    self.add_asteroid(self._ship, size)
                if self.frame_count > SHIELD_TIME:
                    self._ship = None
                # sound playing
                self._sound['blast1'].play()

                break

            i += 1


    def add_asteroid(self, other, size):
        '''

        '''
        x = other.x
        y = other.y
        direction = [other._velocity.x, other._velocity.y]
        # print(direction, 'hi')
        a = math.cos(2*math.pi/3)
        b = math.sin(2*math.pi/3)
        if size == 'medium':
            for i in range(3):
                direction = [(direction[0]*a-direction[1]*b),(direction[0]*b+direction[1]*a)]
                # print(direction)
                small_asteroid = Asteroid(source = 'asteroid3.png', height = 2*SMALL_RADIUS,
                            width = 2*SMALL_RADIUS, x = x, y = y, direction = direction,
                            size = 'small', speed = SMALL_SPEED)
                self._asteroid.append(small_asteroid)                

        elif size == 'large':
            for i in range(3): 
                direction = [(direction[0]*a-direction[1]*b),(direction[0]*b+direction[1]*a)]
                # print(direction)
                medium_asteroid = Asteroid(source = 'asteroid2.png', height = 2*MEDIUM_RADIUS,
                            width = 2*MEDIUM_RADIUS, x = x, y = y, direction = direction,
                            size = 'medium', speed = MEDIUM_SPEED)
                self._asteroid.append(medium_asteroid)
    

    def reset(self):
        data = self._data
        x, y  = self.data['ship']['position']     # position of ship
        angle = self.data['ship']['angle']
        self._ship = Ship(x, y, angle)            # angle of ship
        # print('there')

    
def create_asteroid(asteroids):            # helper function to create asteroids list
    '''
    returns list of asteroids object

    Parameter asteroids: info about asteroids object is here
    Precondition: dictionary having value as list
    '''
    asteroid_list = []
    for i in asteroids:
        x, y = i['position']                 # position of asteroid
        size = i['size']                     # size of asteroid
        direction = i['direction']           # direction of asteroid
        
        if size == 'large':
            asteroid = Asteroid(source = 'asteroid1.png', height = 2*LARGE_RADIUS,
                    width = 2*LARGE_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = LARGE_SPEED)
        
        elif size == 'medium':
            asteroid = Asteroid(source = 'asteroid2.png', height = 2*MEDIUM_RADIUS,
                    width = 2*MEDIUM_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = MEDIUM_SPEED)
        else:
            asteroid = Asteroid(source = 'asteroid3.png', height = 2*SMALL_RADIUS,
                    width = 2*SMALL_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = SMALL_SPEED)

        asteroid_list.append(asteroid)    
    return asteroid_list
    

