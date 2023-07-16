"""
Models module for Planetoids

This module contains the model classes for the Planetoids game. Anything that you
interact with on the screen is model: the ship, the bullets, and the planetoids.

We need models for these objects because they contain information beyond the simple
shapes like GImage and GEllipse. In particular, ALL of these classes need a velocity
representing their movement direction and speed (and hence they all need an additional
attribute representing this fact). But for the most part, that is all they need. You
will only need more complex models if you are adding advanced features like scoring.

You are free to add even more models to this module. You may wish to do this when you
add new features to your game, such as power-ups. If you are unsure about whether to
make a new class or not, please ask on Ed Discussions.

Ranjan Singh
Date 16 may 2023
"""
from consts import *
from game2d import *
from introcs import *
import math

# PRIMARY RULE: Models are not allowed to access anything in any module other than
# consts.py. If you need extra information from Gameplay, then it should be a 
# parameter in your method, and Wave should pass it as a argument when it calls 
# the method.

# START REMOVE
# HELPER FUNCTION FOR MATH CONVERSION
def degToRad(deg):
    """
    Returns the radian value for the given number of degrees
    
    Parameter deg: The degrees to convert
    Precondition: deg is a float
    """
    return math.pi*deg/180

def distance(x1, y1, x2, y2):
    '''
    returns distance bw point(x1, y1) and point(x2, y2)

    Parameter x1: x-axis of first point in cartessian form
    Precondition: float

    Parameter y1: y-axis of first point in cartessian form
    Precondition: float

    Parameter x2: x-axis of second point in cartessian form
    Precondition: float

    Parameter y1: y-axis of second point in cartessian form
    Precondition: float
    '''
    return math.sqrt((x2-x1)**2+(y2-y1)**2)


# END REMOVE


class Bullet(GEllipse):
    """
    A class representing a bullet from the ship
    
    Bullets are typically just white circles (ellipses). The size of the bullet is 
    determined by constants in consts.py. However, we MUST subclass GEllipse, because 
    we need to add an extra attribute for the velocity of the bullet.
    
    The class Wave will need to look at this velocity, so you will need getters for
    the velocity components. However, it is possible to write this assignment with no 
    setters for the velocities. That is because the velocity is fixed and cannot change 
    once the bolt is fired.
    
    In addition to the getters, you need to write the __init__ method to set the starting
    velocity. This __init__ method will need to call the __init__ from GEllipse as a
    helper. This init will need a parameter to set the direction of the velocity.
    
    You also want to create a method to update the bolt. You update the bolt by adding
    the velocity to the position. While it is okay to add a method to detect collisions
    in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    
    # Attribute _velocity: velocity in x direction
    # Invariant: float
    

    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def velocity(self):
        return self._velocity

        
    # INITIALIZER TO SET THE POSITION AND VELOCITY
    def __init__(self, x, y, color, angle):
        """
        Initializes a bullet at (x,y) with velocity of magnitude
        BULLET_SPEED, direction in given angle and color as BULLET_COLOR.

        Parameter x: the starting x-coordinate
        Precondition: x is a number (int or float)

        Parameter y: the starting y-coordinate
        Precondition: y is a number (int or float)

        Parameter color: the bullet color
        Precondition: color is a valid color object or name (e.g. a string)
        
        Parameter angle: direction of bullet to be fired
        Precondition: int, float(in radian only i.e. 0 to 2*pi)
        """
        super().__init__(x=x, y=y, width=2*BULLET_RADIUS,height=2*BULLET_RADIUS,
                                        fillcolor=color, angle = degToRad(angle))
        

    # ADDITIONAL METHODS (MOVEMENT, COLLISIONS, ETC)
    def fire(self):
        '''
        fires or moves the bullets

        first of all it initiallise velocity attribute then change
        pos of bullet as per velocity
        '''
        speed = BULLET_SPEED
        rad_angle = self.angle
        self._velocity = Vector2(speed*math.cos(rad_angle), speed*math.sin(rad_angle))
        self.x += self._velocity.x
        self.y += self._velocity.y


    def is_collided(self, other):
        '''
        returns true if it has collided with other

        precondition: other is a Gimage instance
        '''
        radius1 = self.height/2                              # radius of bullet
        radius2 = other.height/2                             # radius of gimage object
        dist_bw_cent = distance(self.x, self.y, other.x, other.y)
        return radius1+radius2 > dist_bw_cent



class Ship(GImage):
    """
    A class to represent the game ship.
    
    This ship is represented by an image. The size of the ship is determined by constants 
    in consts.py. However, we MUST subclass GEllipse, because we need to add an extra 
    attribute for the velocity of the ship, as well as the facing vecotr (not the same)
    thing.
    
    The class Wave will need to access these two values, so you will need getters for 
    them. But per the instructions,these values are changed indirectly by applying thrust 
    or turning the ship. That means you won't want setters for these attributes, but you 
    will want methods to apply thrust or turn the ship.
    
    This class needs an __init__ method to set the position and initial facing angle.
    This information is provided by the wave JSON file. Ships should start with a shield
    enabled.
    
    Finally, you want a method to update the ship. When you update the ship, you apply
    the velocity to the position. While it is okay to add a method to detect collisions 
    in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # Attribute _velocity: The direction and speed the ship is travelling
    # Invariant: Vector2 object

    # Attribute _facing: The direction the ship is facing
    # Invariant: Vector2 object
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def facing(self):
        return self._facing

    @property
    def velocity(self):
        return self._velocity
    
    
    # INITIALIZER TO CREATE A NEW SHIP
    def __init__(self, x, y, angle):
        super().__init__(source = SHIP_IMAGE, height = 2*SHIP_RADIUS,
                    width = 2*SHIP_RADIUS, x = x, y = y, angle = angle)
        self._velocity = Vector2(0, 0)
        rad_angle = degToRad(angle)
        self._facing   = Vector2(math.cos(rad_angle), math.sin(rad_angle))

    # ADDITIONAL METHODS (MOVEMENT, COLLISIONS, ETC)
    def turn(self, inp):
        '''
        turns the ship according to input received

        Parameter inp: input given to act accordingly
        Precondition: Ginput object
        '''
        if inp.is_key_down('left'):
            self.angle += SHIP_TURN_RATE
        elif inp.is_key_down('right'):
            self.angle -= SHIP_TURN_RATE
        rad_angle = degToRad(self.angle)
        self._facing = Vector2(math.cos(rad_angle), math.sin(rad_angle))

    def impulse(self, inp):
        '''
        gives impulse to Ship and moves the Ship according to input received

        Parameter inp: input given to act accordingly
        Precondition: Ginput object
        '''
        vel_incr = self.facing * SHIP_IMPULSE
        if inp.is_key_down('up'):
            self._velocity += vel_incr
            if self._velocity.length() > SHIP_MAX_SPEED:
                self._velocity = self._velocity.normalize() * SHIP_MAX_SPEED

        self.x += self._velocity.x
        self.y += self._velocity.y

    def wrap(self):
        '''
        wrap Ship around screen

        whenever ship goes off screen it brings back
        ship from the opposite of the screen
        '''

        # horizontal wrapping
        if self.x < -DEAD_ZONE:
            self.x = GAME_WIDTH

        if self.x > GAME_WIDTH + DEAD_ZONE:
            self.x = 0
        
        # vertical wrapping
        if self.y < -DEAD_ZONE:
            self.y = GAME_HEIGHT

        if self.y > GAME_HEIGHT + DEAD_ZONE:
            self.y = 0

    def is_collided(self, other):
        '''
        returns true if it has collided with other
        
        Parameter other: it is another model object which may collide
        Precondition: other is a Gimage instance
        '''
        radius1 = self.height/2    # radius of ship
        radius2 = other.height/2   # radius of gimage object
        dist_bw_cent = distance(self.x, self.y, other.x, other.y)
        return radius1+radius2 > dist_bw_cent 


class Asteroid(GImage):
    """
    A class to represent a single asteroid.
    
    Asteroids are typically are represented by images. Asteroids come in three 
    different sizes (SMALL_ASTEROID, MEDIUM_ASTEROID, and LARGE_ASTEROID) that 
    determine the choice of image and asteroid radius. We MUST subclass GImage, because 
    we need extra attributes for both the size and the velocity of the asteroid.
    
    The class Wave will need to look at the size and velocity, so you will need getters 
    for them.  However, it is possible to write this assignment with no setters for 
    either of these. That is because they are fixed and cannot change when the planetoid 
    is created. 
    
    In addition to the getters, you need to write the __init__ method to set the size
    and starting velocity. Note that the SPEED of an asteroid is defined in const.py,
    so the only thing that differs is the velocity direction.
    
    You also want to create a method to update the asteroid. You update the asteroid 
    by adding the velocity to the position. While it is okay to add a method to detect 
    collisions in this class, you may find it easier to process collisions in wave.py.
    """
    # LIST ANY ATTRIBUTES (AND THEIR INVARIANTS) HERE IF NECESSARY
    # Attribute _velocity: The direction and speed the ship is travelling
    # Invariant: Vector2 object

    # Attribute size: size of the asteroid
    # Invariant: 'large', 'medium', 'small'
    
    # GETTERS AND SETTERS (ONLY ADD IF YOU NEED THEM)
    @property
    def size(self):
        return self._size
    
    
    # INITIALIZER TO CREATE A NEW ASTEROID
    def __init__(self,**keywords):
        super().__init__(**keywords)
        self._size = keywords['size']

        # setting velocity
        direction = keywords['direction']
        speed = keywords['speed']
        if direction[0] != 0 or direction[1] != 0:
            unit_dir_vect = Vector2(direction[0], direction[1]).normalize()
        else:
            unit_dir_vect = Vector2(direction[0], direction[1])
        self._velocity = speed*unit_dir_vect

    
    # ADDITIONAL METHODS (MOVEMENT, COLLISIONS, ETC)
    def move(self):
        '''
        moves the asteroid with given velocity
        '''
        self.x += self._velocity.x
        self.y += self._velocity.y

    def wrap(self):
        '''
        wrap asteroid around screen

        whenever asteroid goes off screen it brings back
        asteroid from the opposite of the screen
        '''

        # horizontal wrapping
        if self.x < -DEAD_ZONE:
            self.x = GAME_WIDTH

        if self.x > GAME_WIDTH + DEAD_ZONE:
            self.x = 0
        
        # vertical wrapping
        if self.y < -DEAD_ZONE:
            self.y = GAME_HEIGHT

        if self.y > GAME_HEIGHT + DEAD_ZONE:
            self.y = 0


# IF YOU NEED ADDITIONAL MODEL CLASSES, THEY GO HERE