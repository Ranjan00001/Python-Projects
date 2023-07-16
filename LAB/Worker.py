class worker(object):
    '''
    '''
    def __init__(self,x,y,z):
        self.ssn = x
        self.lname = y
        self.boss = z

    def __repr__(self):
        # return str(self.__class__)+str(self)
        return str(self.__class__)+'('+str(self.ssn)+', '+str(self.lname)+', '+str(self.boss)+')'
    
# w = worker(123,'singh','self')
# w.ssn = 123
# w.lname = 'university'
# print(w.boss) #= None

# class datetime(object):
#     """docstring for datetime"""
#     def __init__(self, arg):
#         # super datetime, self).__init__()
#         self.arg = arg
