"""
Steganography methods for the imager application.

This module provides all of the test processing operations (encode, decode) 
that are called by the application. Note that this class is a subclass of Filter. 
This allows us to layer this functionality on top of the Instagram-filters, 
providing this functionality in one application.

Based on an original file by Dexter Kozen (dck10) and Walker White (wmw2)

Ranjan Singh
13 Apr.23
"""
import a6filter


class Encoder(a6filter.Filter):
    """
    A class that contains a collection of image processing methods
    
    This class is a subclass of Filter.  That means it inherits all of the 
    methods and attributes of that class too. We do that separate the 
    steganography methods from the image filter methods, making the code
    easier to read.
    
    Both the `encode` and `decode` methods should work with the most recent
    image in the edit history.
    """
    
    def encode(self, text):
        """
        Returns True if it could hide the text; False otherwise.
        
        This method attemps to hide the given message text in the current 
        image. This method first converts the text to a byte list using the 
        encode() method in string to use UTF-8 representation:
            
            blist = list(text.encode('utf-8'))
        
        This allows the encode method to support all text, including emoji.
        
        If the text UTF-8 encoding requires more than 999999 bytes or the 
        picture does  not have enough pixels to store these bytes this method
        returns False without storing the message. However, if the number of
        bytes is both less than 1000000 and less than (# pixels - 10), then 
        the encoding should succeed.  So this method uses no more than 10
        pixels to store additional encoding information.
        
        Parameter text: a message to hide
        Precondition: text is a string
        """
        # You may modify anything in the above specification EXCEPT
        # The first line (Returns True...)
        # The last paragraph (If the text UTF-8 encoding...)
        # The precondition (text is a string)

        assert type(text) == str, repr(text)+' is invalid'

        current = self.getCurrent()
        blist = list(text.encode('utf-8'))

        if 0 > len(blist) >= 999999 or len(blist) > len(current) - 10:
            return False
        else:
            self._encode_pixel(ord('y'),1)
            self._encode_pixel(ord('a'),2)   # stored info for text is encodable or not

        len_in_str = str(len(text))
        len_encode = '0' * (6 - len(len_in_str)) + len_in_str
        for i in range(6):
            self._encode_pixel(ord(len_encode[i]), i+3)    # stored info about length of text in 3 to 9 pixel

        for i in range(len(blist)):
            self._encode_pixel(blist[i], i+10)

        return True
    
    def decode(self):
        """
        Returns the secret message (a string) stored in the current image.
        
        The message should be decoded as a list of bytes. Assuming that a list
        blist has only bytes (ints in 0.255), you can turn it into a string
        using UTF-8 with the decode method:
            
            text = bytes(blist).decode('utf-8')
        
        If no message is detected, or if there is an error in decoding the
        message, this method returns None
        """
        # You may modify anything in the above specification EXCEPT
        # The first line (Returns the secret...)
        # The last paragraph (If no message is detected...)
        
        current = self.getCurrent()
        if self._decode_pixel(1) != ord('y') or self._decode_pixel(2) != ord('a'):   # checks if pixel is decodable or not
            return None

        length = self.func()
        blist = []
        for  x in range(10, int(length)+10):
            num = self._decode_pixel(x)
            # print(x, num)
            if num <= 256:
                blist.append(num)
            else:
                return None

        return bytes(blist).decode('utf-8')

    # HELPER METHODS  (dealing 1-d list)
    def _decode_pixel(self, pos):
        """
        Return: the number n hidden in pixel pos of the current image.
        
        This function assumes that the value was a 3-digit number encoded as 
        the last digit in each color channel (e.g. red, green and blue).
        
        Parameter pos: a pixel position
        Precondition: pos is an int with  0 <= p < image length (as a 1d list)
        """
        # This is helper. You do not have to use it. You are allowed to change it.
        # There are no restrictions on how you can change it.

        current = self.getCurrent()
        assert pos < len(current) - 10, repr(pos) + ' is invalid'

        rgb = current[pos]
        red   = rgb[0]
        green = rgb[1]
        blue  = rgb[2]
        return  (red % 10) * 100  +  (green % 10) * 10  +  blue % 10

    def _encode_pixel(self, num, pos):
        '''
        sets the pixel with the text corresponding to given num at that pos

        parameter num: ascii corresponding to the str we want to hide
        precondition: num < 256

        parameter pos: position at which we want to hide the str
        precondition: pos <= len(self.getCurrent()) - 10
        '''
        current = self.getCurrent()
        assert pos < len(current) - 10, repr(pos) + ' is invalid'
        
        rgb = self.getCurrent()[pos]
        # print('before',rgb)
        red = rgb[0] - (rgb[0] % 10) + num // 100
        grn = rgb[1] - (rgb[1] % 10) + (num // 10) % 10    # this is for accesing middle element of a three digit number
        blu = rgb[2] - (rgb[2] % 10) + num % 10
        
        red = red if red <= 255 else red - 10
        grn = grn if grn <= 255 else grn - 10
        blu = blu if blu <= 255 else blu - 10

        rgb = (red, grn, blu)
        current._data[pos] = rgb
        

    def func(self):
        '''
        returns the length of text that has been encoded to pixel

        note that messge about length is in pixel 3-9
        '''
        current = self.getCurrent()
        result  = ''
        for i in range(3,9):
            a = self._decode_pixel(i)
            result += chr(a)
        # print('res', result)
        return result
