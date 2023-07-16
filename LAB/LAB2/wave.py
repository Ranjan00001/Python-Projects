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

# YOUR NAME(S) AND NETID(S) HERE
# DATE COMPLETED HERE
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
    
    def hasShip(self):
        """
        Returns: True if there is a ship on the screen; False otherwise
        """
        return not self._ship is None


    # def hasWon(self):
    #     """
    #     Return: Whether the player has completed the wave.

    #     Completing the wave requires all aliens to be killed.
    #     """
    #     return self._lives == 0

    # def hasLost(self):
    #     """
    #     Return: Whether the player has lost the game.

    #     The player looses if all lives are gone OR the aliens break the defense line.
    #     """
    #     return self._ship == None and self._lives <= 0
    

    # INITIALIZER (standard form) TO CREATE SHIP AND ASTEROIDS
    def __init__(self,data):
        """
        Initializer: Creates a new wave 
        """
        # Required attributes

        self._data = data
        self._lives = SHIP_LIVES

        # creating ship
        x, y  = self._data['ship']['position']
        angle = self._data['ship']['angle']
        self._ship = Ship(x, y, angle)
        
        # creating asteroids
        self._init_asteroids(data['asteroids'])

        # bullets
        self._bullets = []
        #self._firerate = 0



    # UPDATE METHOD TO MOVE THE SHIP, ASTEROIDS, AND BULLETS
    def update(self,input):
        """
        Updates the wave by one animation frame.

        This method does the following:
            * It moves the ship according to input
            * 
        
        Parameter input: The Player input
        Precondition: input is a GInput

        Parameter dt: The time since the last frame
        Precondition: dt is a float >= 0
        """
        self._update_ship_(input)
        self._update_asteroids()
        self._update_bullets(input)

    
    # DRAW METHOD TO DRAW THE SHIP, ASTEROIDS, AND BULLETS
    def draw(self,view):
        """
        Draws the ship, planetoids, and bullets to the screen.

        Parameter view: The view to draw to
        Precondition: view is a GView
        """
        if self._ship:
            self._ship.draw(view)

        for ast in self._asteroids:
            ast.draw(view)

        for bul in self._bullets:
            bul.draw(view)



    # RESET METHOD FOR CREATING A NEW LIFE
    def reset(self):
        """
        Creates a new ship so we can continue with the wave
        """
        self._ship = Ship()
    
    # HELPER METHODS FOR PHYSICS AND COLLISION DETECTION
    def _update_ship_(self,input):
        """
        Moves the ship according to user input.
        
            
        It also processes requests to fire the bullet.  However, the player may only
        have one  bullet on screen at a time.
        
        Parameter dt: The time since the last frame
        Precondition: dt is a float >= 0
        
        Parameter input: The user input
        Precondition: input is a GInput
        """
        # if not self._ship or self._ship.isDeleted():
        #     return
        # elif self._ship.isDying():
        #     try:
        #         self._boom.send(dt)
        #     except:
        #         self._ship = None
        #         self._lives -= 1
        #         self._bolts = []
        #     return

        da = 0

        if input.is_key_down('right'):
            da -= SHIP_TURN_RATE
            self._ship.turn(da)
        if input.is_key_down('left'):
            da += SHIP_TURN_RATE
            self._ship.turn(da)

        if input.is_key_down('up'):
            print("yes")
            self._ship.applyImpulse()

        self._ship.move()
        self._ship.wrap()

        # fire = input.is_key_down('up') or input.is_key_down('spacebar')
        # if fire and not self._fire:
        #     self._fire = True
        #     found = False

        #     for bolt in self._bolts:
        #         if bolt.isShipBolt():
        #             found = True

        #     if not found:
        #         bolt = Bolt(self._ship.x,self._ship.y+self._ship.height/2,10)
        #         self._bolts.append(bolt)
        # elif self._fire and not fire:
        #     self._fire = False

    
    def _update_asteroids(self):
        for ast in self._asteroids:
            ast.move()
            ast.wrap()


    def _update_bullets(self,input):
        #self._firerate += 1
        #if input.is_key_down('spacebar') and self._firerate%BULLET_RATE == 0:
        if input.is_key_down('spacebar'):
            #print("pressed")
            bullet_position = self._ship._facing * SHIP_RADIUS + Vector2(self._ship.x, self._ship.y)
            self._bullets.append(Bullet(x=bullet_position.x, y=bullet_position.y, color=BULLET_COLOR, angle=self._ship.angle))
            #self._bullets.append(Bullet(x=GAME_WIDTH/2, y=GAME_WIDTH/2, color=BULLET_COLOR, angle=self._ship.angle))



    # helper function to create asteroids list
    def _init_asteroids(self,asteroids):
        '''
        returns list of asteroids object

        Parameter asteroids: info about asteroids object is here
        Precondition: dictionary having value as list
        '''
        asteroid_list = []
        for ast in asteroids:
            x, y = ast['position']                 # position of asteroid
            size = ast['size']                     # size of asteroid
            direction = ast['direction']           # direction of asteroid
        
            if size == 'large':
                asteroid = Asteroid(source = LARGE_IMAGE, height = 2*LARGE_RADIUS,
                    width = 2*LARGE_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = LARGE_SPEED)
        
            elif size == 'medium':
                asteroid = Asteroid(source = MEDIUM_IMAGE, height = 2*MEDIUM_RADIUS,
                    width = 2*MEDIUM_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = MEDIUM_SPEED)
            else:
                asteroid = Asteroid(source = SMALL_IMAGE, height = 2*SMALL_RADIUS,
                    width = 2*SMALL_RADIUS, x = x, y = y, direction = direction,
                    size = size, speed = SMALL_SPEED)

            asteroid_list.append(asteroid)
            self._asteroids = asteroid_list
    




        
