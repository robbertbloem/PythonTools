import numpy



# SIMPLE EQUATIONS
def polynomial(A, x):
    """
    Polynomial
    
    ::
    
        y = A[0] + A[1] * x + A[2] * x^2 + A[3] * x^3 + ... + A[n-1] * x^{n-1}
    
    Arguments
    ---------
    A : array-like 
        List with coefficients. A[0] is an offset.
    x : array
        Variable
        
    """
    x = numpy.asarray(x)
    y = 0
    for i in range(len(A)):
        y += A[i] * x**i
    return y


# GONIOMETRIC
def cos(A, x):
    """
    Cosine
    
    ::
    
        y = A[0] + A[1] * cos(2 * pi * A[2] * x + A[3])

    - A[0]: offset
    - A[1]: amplitude
    - A[2]: frequency
    - A[3]: phase
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable  
        
    """
    x = numpy.asarray(x)
    if len(A) != 4:
        raise IndexError("PythonTools.Equations.cos(): you should enter 4 parameters in list A.")
    return A[0] + A[1] * numpy.cos(2 * numpy.pi * A[2] * x + numpy.pi*A[3])



# EXPONENTIAL DECAYS
def single_exp(A,x):
    """
    Single exponential decay. For a single exponential with an offset, use `single_exp_offset`.

    ::
    
        y = A[0] * exp(-x / A[1]) 

    - A[0]: Amplitude
    - A[1]: Decay rate        
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable   
        
    """
    x = numpy.asarray(x)
    if len(A) != 2:
        raise IndexError("PythonTools.Equations.single_exp(): you should enter 2 parameters in list A.")    
    return A[0] * numpy.exp(-x / A[1]) 


def double_exp(A,x):
    """
    
    ::

        y = A[0] * exp(-x / A[1]) + A[2] * exp(-x / A[3])

    - A[0]: Amplitude exponential 1
    - A[1]: Decay rate exponential 1
    - A[2]: Amplitude exponential 2
    - A[3]: Decay rate exponential 2           
        
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable   
    
    """
    x = numpy.asarray(x)
    if len(A) != 4:
        raise IndexError("PythonTools.Equations.double_exp(): you should enter 4 parameters in list A.")    
    return A[0] * numpy.exp(-x / A[1]) + A[2] * numpy.exp(-x / A[3])


def single_exp_offset(A,x):
    """
    Single exponential with offset. For an exponential decay without offset, use `single_exp`.
    ::
        
        y = A[0] * exp(-x / A[1]) + A[2]

    - A[0]: Amplitude
    - A[1]: Decay rate
    - A[2]: Offset            
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable   
    
    """
    x = numpy.asarray(x)
    if len(A) != 3:
        raise IndexError("PythonTools.Equations.single_exp_offset(): you should enter 3 parameters in list A.")    
    return A[0] * numpy.exp(-x / A[1]) + A[2]


# DISTRIBUTIONS
def gaussian(A, x):
    """
    Gaussian
    
    ::
    
        a = A[3] / (A[0] * sqrt(2 * pi))
        b = exp( -(x - A[1])**2 / (2 * A[0]**2) )
        y = a * b + A[2]

    - A[0]: sigma (sigma^2 = variance)
    - A[1]: mu (mean)
    - A[2]: offset 
    - A[3]: scale, before offset
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable       

    """
    x = numpy.asarray(x)
    if len(A) != 4:
        raise IndexError("PythonTools.Equations.gaussian(): you should enter 4 parameters in list A.")    
    return ( A[3] / (A[0] * numpy.sqrt(2*numpy.pi)) ) * numpy.exp( -(x - A[1])**2 / (2 * A[0]**2) ) + A[2]


def gaussian_2d(A, x, y):
    """
    
    - A[0]: sigma x
    - A[1]: mu x
    - A[2]: sigma y
    - A[3]: mu y   
    - A[4]: theta (rotation)
    - A[5]: amplitude
    
    
    """
    X, Y = numpy.meshgrid(x, y)
    sigma_X = A[0]
    X -= A[1]
    sigma_Y = A[2]
    Y -= A[3]
    theta = A[4]
    A = A[5]

    if theta == 0:
        a = 1 / (2 * sigma_X**2) 
        b = 0
        c = 1 / (2 * sigma_Y**2)
    else:
        a = numpy.cos(theta)**2 / (2 * sigma_X**2) + numpy.sin(theta)**2/(2 * sigma_Y**2)
        b = -numpy.sin(2 * theta) / (4 * sigma_X**2) + numpy.sin(2 * theta) / (4 * sigma_Y**2)
        c = numpy.sin(theta)**2/(2 * sigma_X**2) + numpy.cos(theta)**2 / (2 * sigma_Y**2)
    
    return A * numpy.exp( -(a * X**2 + 2 * b * X * Y + c * Y**2))
    
    
    
    

def lorentzian(A, x):
    """
    Lorentzian
    
    ::
    
        y = A[3]/(pi * A[0] * (1 + ((x - A[1])/A[0])**2)) + A[2]
        
    - A[0]: gamma
    - A[1]: mean
    - A[2]: offset
    - A[3]: scale        
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable       

    """
    x = numpy.asarray(x)
    if len(A) != 4:
        raise IndexError("PythonTools.Equations.lorentzian(): you should enter 4 parameters in list A.")    
    return A[3]/(numpy.pi * A[0] * (1 + ((x - A[1])/A[0])**2)) + A[2]


def double_lorentzians(A, x):
    """
    Two Lorentzians
    
    ::
    
        y1 = A[3]/(pi * A[0] * (1 + ((x - A[1])/A[0])**2)) + A[2]
        y2 = A[7]/(pi * A[4] * (1 + ((x - A[5])/A[4])**2)) + A[6]
        y = y1 + y2
        
    - A[0]: gamma Lorentzian 1
    - A[1]: mean Lorentzian 1
    - A[2]: offset Lorentzian 1
    - A[3]: scale Lorentzian 1
    - A[4]: gamma Lorentzian 2
    - A[5]: mean Lorentzian 2
    - A[6]: offset Lorentzian 2
    - A[7]: scale Lorentzian 2           
        
    Arguments
    ---------
    A : array-like 
        List with coefficients. 
    x : array
        Variable       
    
    """
    x = numpy.asarray(x)
    if len(A) != 8:
        raise IndexError("PythonTools.Equations.double_lorentzians(): you should enter 8 parameters in list A.")    
    return lorentzian(A[:4], x) + lorentzian(A[4:], x)