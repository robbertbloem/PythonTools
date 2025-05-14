



# SIMPLE EQUATIONS
def polynomial(A, t):
    """
    
    """
    y = 0
    for i in range(len(A)):
        y += A[i] * t**i
    return y


# GONIOMETRIC
def cos(A, t):
    """
    4 parameters
    function: A[0] + A[1] * numpy.cos(2 * numpy.pi * A[2] * t + A[3])
    A[0]: offset
    A[1]: amplitude
    A[2]: frequency
    A[3]: phase
    """
    A = CF.make_numpy_ndarray(A)
    if len(A) != 4:
        raise IndexError("rb_cos(): you should enter 4 parameters in list A.")
    t = CF.make_numpy_ndarray(t)
    return A[0] + A[1] * numpy.cos(2 * numpy.pi * A[2] * t + numpy.pi*A[3])



# EXPONENTIAL DECAYS
def exp(A,t):
    return A[0] * numpy.exp(-t / A[1]) 


def double_exp(A,t):
    return A[0] * numpy.exp(-t / A[1]) + A[2] * numpy.exp(-t / A[3])


def single_exp_offset(A,t):
    return A[0] * numpy.exp(-t / A[1]) + A[2]


# DISTRIBUTIONS
def gaussian(A, t):
    """
    A[0]: sigma (sigma^2 = variance)
    A[1]: mu (mean)
    A[2]: offset 
    A[3]: scale, before offset

    """
    y = ( A[3] / (A[0] * numpy.sqrt(2*numpy.pi)) ) * numpy.exp( -(t - A[1])**2 / (2 * A[0]**2) ) + A[2]
    return y


def lorentzian(A, t):
    """
    A[0]: gamma
    A[1]: mean
    A[2]: offset
    A[3]: scale
    """

    return A[3]/(numpy.pi * A[0] * (1 + ((t - A[1])/A[0])**2)) + A[2]


def two_lorentzians(A, t):

    return rb_lorentzian(A[:4], t) + rb_lorentzian(A[4:], t)