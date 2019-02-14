import numpy
import matplotlib 
import matplotlib.pyplot as plt


def make_numpy_ndarray(val):
    """
    make a numpy.ndarray out of val, used by make_coordinates()
    
    Types of val that are accepted:        
    int, float, string: make it a list and then numpy.ndarray.
    list: make it a numpy.ndarray
    tuple: convert to a list, then numpy.ndarray
    numpy.ndarray: return directly
    
    Not accepted:
    dict
    
    CHANGELOG:
    20130317/RB: started
    20190214/RB: changed call to DEBUG with a simple print statement
    """
            
    if type(val) == numpy.ndarray:
        return val
    elif type(val) == list:
        return numpy.array(val)
    elif type(val) == dict:
        print("Value shouldn't be a dict or tuple")
        return False
    elif type(val) == tuple:
        return numpy.array(list(val))
    else:
        return numpy.array([val])  
        

def find_longest_list(*kwargs):

    """
    Helper function to find the longest in a series of lists.
    It does not check if it is actually a list.
    Used by make_coordinates()
    
    CHANGELOG:
    20130317/RB: started
    
    """
    
    length = 0
    
    for l in kwargs:        
        temp = len(l)
        if temp > length:
            length = temp
    
    return length


def make_coordinates(inch_per_unit, x_units, y_units, left, bottom, width, 
height, flag_verbose = False):
    
    """
    
    matplotlib.figure.add_axes() requires coordinates (left, bottom, width, 
    height) for each axes instance. The values are between 0 and 1. There are 
    two problems. 
    
    First is that the aspect ratio may be off. If the figure is a rectangle and 
    the subplot is 0.5 wide and 0.5 high, the subplot is also a rectangle. 
    Second is that if the figure size changes all the carefully planned margins 
    are lost. 
    
    This function works with units. The x-axis is x_units long. Each unit has a 
    defined length inch_per_unit. The left edges are at [left]. This solves the 
    two problems. If your plot is N units wide and N units high, it will be a 
    square. When you resize the figure (change x_units) the margins, which are 
    in units, will remain the same.     
    
    INPUT:
    - inch_per_unit (number): used to scale to inches
    - x_units, y_units (number): width and height of the figure, in units
    - left, bottom, width, height (numpy.ndarray with ints and/or floats, also 
    accepts list or int or float): the positions of the axes. The longest list 
    determines the number of plots. Shorter lists are cycled. 
    
    OUTPUT:
    - figsize: tuple that is accepted by plt.figure(figsize = figsize)
    - coords, a list with tuples with (l,b,w,h). The tuples are accepted by 
    fig.add_axes((l,b,w,h)). 

   
    EXAMPLE 1:

    Three plots next to each other. 
    
    01234567
    1 x  x x
    0xxxxxxx
    
    x_units = 8
    y_units = 3
    left = [1,3,6]  #
    bottom = 1      # [1], [1,1], [1,1,1] 
                    # not [1,1,1,1], that gives extra subplot
    width = [1,2]   # [1,2,1]
    height = 1      # [1], [1,1], [1,1,1]
    
    
    EXAMPLE 2:
    
    Four equally sized and spaced plots.
    
    01234
    3 x x
    2xxxx
    1 x x 
    0xxxx
    
    inch_per_unit = 1.0
    x_units = 5
    y_units = 5
    left = [1,3]        # [1,3,1,3]
                        # not [1,3,1], that would give: [1,3,1,1]
    bottom = [3,3,1,1]  #
    width = 1           # [1], [1,1], [1,1,1], [1,1,1,1]
    height = 1          # [1], [1,1], [1,1,1], [1,1,1,1]
    

    EXAMPLE 3:
        
    A complex arrangement. All coordinates are explicitly given. 
    
    01234567
    6   x  x
    5   x  x
    4xxxx  x
    3  xxxxx
    2  x   x
    1  x   x
    0xxxxxxx   

    x_units = 8
    y_units = 8
    left = [1,5,1,4]
    bottom = [5,4,1,1]
    width = [3,2,2,3]
    height = [2,3,3,2]    
    
    
    
    CHANGELOG:
    20130317/RB: started   
    
     
    """ 
    # calculate figure size
    figsize = (x_units * inch_per_unit, y_units * inch_per_unit)

    # change all values to values between 0 and 1
    left = make_numpy_ndarray(left) / x_units
    bottom = make_numpy_ndarray(bottom) / y_units
    width = make_numpy_ndarray(width) / x_units
    height = make_numpy_ndarray(height) / y_units
    
    # find longest list, determines number of sub plots
    N = find_longest_list(left, bottom, width, height)
    
    # determine the coordinates
    coords = []
    for i in range(N):
        
        l = left[i % len(left)]
        b = bottom[i % len(bottom)]
        w = width[i % len(width)]
        h = height[i % len(height)]
        
        coords.append((l,b,w,h))
        
    return figsize, coords
    


if __name__ == '__main__': 
    pass
    



 