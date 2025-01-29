dfs'''
A Module for define a Square
'''


class Square:
    '''
    define a simple square and its size
    '''
    def __init__(self, size=0):
        '''
        Initialise a loop for verify if size is an integer
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        '''
        Initialise a loop for verify if size is less than 0
        '''
        if size < 0:
            raise ValueError("size must be >= 0")
        '''
        Initialise size of square
        '''
        self.__size = size
    '''
    define area of a square
    '''
    def area(self):
        '''
        return the square of size
        '''
        return self.__size ** 2
