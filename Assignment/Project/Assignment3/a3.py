""" 
Functions for Assignment A3

This file contains the functions for the assignment. You should replace the stubs
with your own implementations.

RANJAN SINGH
DATE-23/02/2023

"""
import introcs
import math


def complement_rgb(rgb):
    """
    Returns the complement of color rgb.
    
    Parameter rgb: the color to complement
    Precondition: rgb is an RGB object
    """
    return introcs.RGB(255-rgb.red, 255-rgb.green, 255-rgb.blue)


def str5(value):
    """
    Returns value as a string, but expanded or rounded to be exactly 5 characters.
    
    The decimal point counts as one of the five characters.
   
    Examples:
        str5(1.3546)  is  '1.355'.
        str5(21.9954) is  '22.00'.
        str5(21.994)  is  '21.99'.
        str5(130.59)  is  '130.6'.
        str5(130.54)  is  '130.5'.
        str5(1)       is  '1.000'.
    
    Parameter value: the number to convert to a 5 character string.
    Precondition: value is a number (int or float), 0 <= value <= 360.
    """
    # Remember that the rounding takes place at a different place depending 
    # on how big value is. Look at the examples in the specification.
    value = float(value)
    a = str(value).find('.')+1
    if a == 2:
        value = '%0.3f'%(value)
    elif a == 3:
        value = '%0.2f'%(value)
    elif a == 4:
        value = '%0.1f'%(value)
    elif 'e' in str(value):
        value = '0.000'
    return str(value) if len(str(value)) == 5 else str(value)[:-1]


def str5_cmyk(cmyk):
    """
    Returns the string representation of cmyk in the form "(C, M, Y, K)".
    
    In the output, each of C, M, Y, and K should be exactly 5 characters long.
    Hence the output of this function is not the same as str(cmyk)
    
    Example: if str(cmyk) is 
    
          '(0.0,31.3725490196,31.3725490196,0.0)'
    
    then str5_cmyk(cmyk) is '(0.000, 31.37, 31.37, 0.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter cmyk: the color to convert to a string
    Precondition: cmyk is an CMYK object.
    """
    s = str(cmyk)
    end1 = s.find(',')
    arg1 = float(s[s.find('(')+1:end1])
    end2 = s.find(',',end1+1)
    arg2 = float(s[end1+1:end2])
    end3 = s.find(',',end2+1)
    arg3 = float(s[end2+1:end3])
    end4 = s.find(')')
    arg4 = float(s[end3+1:end4])
    return '('+str5(arg1)+', '+str5(arg2)+', '+str5(arg3)+', '+str5(arg4)+')'


def str5_hsv(hsv):
    """
    Returns the string representation of hsv in the form "(H, S, V)".
    
    In the output, each of H, S, and V should be exactly 5 characters long.
    Hence the output of this function is not the same as str(hsv)
    
    Example: if str(hsv) is 
    
          '(0.0,0.313725490196,1.0)'
    
    then str5_hsv(hsv) is '(0.000, 0.314, 1.000)'. Note the spaces after the
    commas. These must be there.
    
    Parameter hsv: the color to convert to a string
    Precondition: hsv is an HSV object.
    """
    s = str(hsv)
    end1 = s.find(',')
    arg1 = float(s[s.find('(')+1:end1])
    end2 = s.find(',',end1+1)
    arg2 = float(s[end1+1:end2])
    end3 = s.find(')')
    arg3 = float(s[end2+1:end3])
    return '('+str5(arg1)+', '+str5(arg2)+', '+str5(arg3)+')'


def rgb_to_cmyk(rgb):
    """
    Returns a CMYK object equivalent to rgb, with the most black possible.
    
    Formulae from https://www.rapidtables.com/convert/color/rgb-to-cmyk.html
    
    Parameter rgb: the color to convert to a CMYK object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to the range 0..1 by dividing them by 255.0.
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    k = 1-max(r,g,b)
    # print(k)
    if k != 1:
        c = (1-r-k)/(1-k)        #float()
        m = (1-g-k)/(1-k)        #float()
        y = (1-b-k)/(1-k)        #float()
        # print(c,m,y)
    else:
        c = m = y = 0.0
    return introcs.CMYK(c*100, m*100, y*100, k*100)


def cmyk_to_rgb(cmyk):
    """
    Returns an RGB object equivalent to cmyk
    
    Formulae from https://www.rapidtables.com/convert/color/cmyk-to-rgb.html
   
    Parameter cmyk: the color to convert to a RGB object
    Precondition: cmyk is an CMYK object.
    """
    # The CMYK numbers are in the range 0.0..100.0. 
    # Deal with them the same way as the RGB numbers in rgb_to_cmyk()
    c = cmyk.cyan/100
    m = cmyk.magenta/100
    y = cmyk.yellow/100
    k = cmyk.black/100
    r = round(255*(1-c)*(1-k))
    g = round(255*(1-m)*(1-k))
    b = round(255*(1-y)*(1-k))
    return introcs.RGB(r, g, b)


def rgb_to_hsv(rgb):
    """
    Return an HSV object equivalent to rgb
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
   
    Parameter hsv: the color to convert to a HSV object
    Precondition: rgb is an RGB object
    """
    # The RGB numbers are in the range 0..255.
    # Change them to range 0..1 by dividing them by 255.0.
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    maximum = max(r,g,b)
    minimum = min(r,g,b)
    if maximum == minimum:
        h = 0
    elif maximum == r and g >= b:
        h = 60.0*(g-b)/(maximum-minimum)
    elif maximum == r and g < b:
        h = 60.0*(g-b)/(maximum-minimum)+360.0
    elif maximum == g:
        h = 60.0*(b-r)/(maximum-minimum)+120.0
    elif maximum == b:
        h = 60.0*(r-g)/(maximum-minimum)+240.0
    s = 0 if maximum == 0 else 1-minimum/maximum
    v = maximum
    return introcs.HSV(float(h),float(s),float(v))


def hsv_to_rgb(hsv):
    """
    Returns an RGB object equivalent to hsv
    
    Formulae from https://en.wikipedia.org/wiki/HSL_and_HSV
    
    Parameter hsv: the color to convert to a RGB object
    Precondition: hsv is an HSV object.
    """
    import math
    h = hsv.hue
    s = hsv.saturation
    v = hsv.value
    hi = math.floor(h/60)
    f = h/60-hi
    p = v*(1-s)
    q = v*(1-f*s)
    t = v*(1-(1-f)*s)
    if hi == 0:
        r = v
        g = t
        b = p
    elif hi == 1:
        r = q
        g = v
        b = p
    elif hi == 2:
        r = p
        g = v
        b = t
    elif hi == 3:
        r = p
        g = q
        b = v
    elif hi == 4:
        r = t
        g = p
        b = v
    elif hi == 5:
        r = v
        g = p
        b = q
    return introcs.RGB(round(r*255),round(g*255),round(b*255))

def contrast_value(value,contrast):
    """
    Returns value adjusted to the "sawtooth curve" for the given contrast
    
    At contrast = 0, the curve is the normal line y = x, so value is unaffected.
    If contrast < 0, values are pulled closer together, with all values collapsing
    to 0.5 when contrast = -1.  If contrast > 0, values are pulled farther apart, 
    with all values becoming 0 or 1 when contrast = 1.
    
    Parameter value: the value to adjust
    Precondition: value is a float in 0..1
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    if -1 <= contrast < 1:
        if value < 0.25*(1+contrast):
            y = ((1-contrast)/(1+contrast))*value
        elif value > 0.75-0.25*contrast:
            y = ((1-contrast)/(1+contrast))*(value-((3-contrast)/4))+((3+contrast)/4)
        else:
            y = ((1+contrast)/(1-contrast))*(value-((1+contrast)/4))+((1-contrast)/4)
    else:
        y = 1 if value >= 0.5 else 0
    return float(y)


def contrast_rgb(rgb,contrast):
    """
    Applies the given contrast to the RGB object rgb
    
    This function is a PROCEDURE.  It modifies rgb and has no return value.  It should
    apply contrast_value to the red, blue, and green values.
    
    Parameter rgb: the color to adjust
    Precondition: rgb is an RGB object
    
    Parameter contrast: the contrast amount (0 is no contrast)
    Precondition: contrast is a float in -1..1
    """
    r = rgb.red/255
    g = rgb.green/255
    b = rgb.blue/255
    rgb.red   = round((contrast_value(r,contrast))*255)
    rgb.green = round((contrast_value(g,contrast))*255)
    rgb.blue  = round((contrast_value(b,contrast))*255)


    