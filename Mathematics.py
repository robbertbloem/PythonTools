from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

import inspect

import numpy

import numpy
import matplotlib 
import matplotlib.pyplot as plt

try:
    from scipy.optimize.minpack import leastsq
    scipy_import = True
except ImportError:
    scipy_import = False

from scipy.interpolate import interp1d

import itertools

import PythonTools.CommonFunctions as CF


### CODE FOR FITTING PROCEDURE ###

def minimize(A, t, y0, function):
    """
    Needed for fit
    """
    return y0 - function(A, t)

def fit(x_array, y_array, function, A_start, return_all = False):
    """
    Fit data
    
    20101209/RB: started
    20130131/RB: imported in Crocodile, added example to doc-string

    INPUT:
    x_array: the array with time or something
    y-array: the array with the values that have to be fitted
    function: one of the functions, in the format as in the file "Equations"
    A_start: a starting point for the fitting
    return_all: the function used to return only the final result. The leastsq method does however return more data, which may be useful for debugging. When the this flag is True, it will return these extras as well. For legacy purposes the default is False. See reference of leastsq method for the extra output: http://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.leastsq.html
    
    OUTPUT:
    A_final: the final parameters of the fitting
    When return_all == True:
    - cov_x (ndarray): Uses the fjac and ipvt optional outputs to construct an estimate of the jacobian around the solution. None if a singular matrix encountered (indicates very flat curvature in some direction). This matrix must be multiplied by the residual variance to get the covariance of the parameter estimates - see curve_fit.
    - infodict (dict): a dictionary of optional outputs with the key s:
        - "nfev" : the number of function calls
        - "fvec" : the function evaluated at the output
        - "fjac" : A permutation of the R matrix of a QR
                 factorization of the final approximate
                 Jacobian matrix, stored column wise.
                 Together with ipvt, the covariance of the
                 estimate can be approximated.
        - "ipvt" : an integer array of length N which defines
                 a permutation matrix, p, such that
                 fjac*p = q*r, where r is upper triangular
                 with diagonal elements of nonincreasing
                 magnitude. Column j of p is column ipvt(j)
                 of the identity matrix.
        - "qtf"  : the vector (transpose(q) * fvec).
    - mesg (str): A string message giving information about the cause of failure.
    - ier (int): An integer flag. If it is equal to 1, 2, 3 or 4, the solution was found. Otherwise, the solution was not found. In either case, the optional output variable "mesg" gives more information.


    EXAMPLE:
    Fit some data to this function from Crocodile.Resources.Equations:
    def linear(A, t):
        return A[0] + A[1] * t  
    
    ### 
    x = x-axis
    y = some data
    A = [0,1] # initial guess
    A_final = fit(x, y, Crocodile.Resources.Equations.linear, A)
    ###
    
    WARNING:
    Always check the result, it might sometimes be sensitive to a good starting point.

    """
    if scipy_import:
        param = (x_array, y_array, function)
    
        A_final, cov_x, infodict, mesg, ier = leastsq(minimize, A_start, args=param, full_output=True)

        if return_all:
            return A_final, cov_x, infodict, mesg, ier
        else:
            return A_final
    else:
        DEBUG.printError("Scipy.leastsq is not loaded. Fit is not done", inspect.stack())
        return False


def correlation_fft(a, v = -1, flag_normalize = True, flag_verbose = False):
    """
    Calculate the autocorrelation using fft.
    
    This method was verified using a naive implementation in C. 
    
    INPUT:
    - a, v (ndarray): the data, 1D array. If v == 1, the autocorrelation of a with a will be calculated. 
    - flag_normalizae (Bool, True): if True, the starting value of the autocorrelation is 1. If not, it is an absolute value.
    - flag_verbose (Bool, False): if True, print some debugging stuff
    
    OUTPUT:
    - autocorrelation of array, normalized to the length or to 1, the real values   
    
    201202xx/RB: started function
    20130205/RB: the function now uses an actual Fourier transform
    20130207/RB: take the first part of the array, not the last part reversed. This was done to agree with Jan's correlation method, but now it seems that one is wrong.
    20130515/RB: the result is now always divided by the length of the array and it gives the actual absolute value. Added some documentation
    20160317/RB: added v, to calculate the correlation between two arrays. 
    
    """
    
#     DEBUG.verbose("correlation_fft", flag_verbose)

    if type(v) != numpy.ndarray:
        v = a[:]

    # by subtracting the mean, the autocorrelation decays to zero
    a -= numpy.mean(a)
    v -= numpy.mean(v)

    l_a = len(a)
    l_v = len(v)
    
    if l_a > l_v:
        l_pad = 2 ** int(1+numpy.log2(l_a * 2))
        l_min = l_v
    else:
        l_pad = 2 ** int(1+numpy.log2(l_v * 2))
        l_min = l_a

    # zeropad to closest 2^n to prevent aliasing
    a = numpy.pad(a, (0, l_pad-l_a), "constant", constant_values = 0)
    v = numpy.pad(v, (0, l_pad-l_v), "constant", constant_values = 0)

    # calculate autocorrelation
    s_a = numpy.fft.fft(a)
    s_v = numpy.conjugate(numpy.fft.fft(v))
    r = numpy.fft.ifft(s_a * s_v)

    # normalize to length
    r = r[:l_min] / l_min

    # return value
    if flag_normalize:
        return numpy.real(r/r[0])
    else:
        return numpy.real(r)

### DERIVATIVE ###

def derivative(x, y):
    """
    20110909/RB: rudimentary method to calculate the derivative
    """

    dx = x[1] - x[0]

    l = len(y)

    x_temp = numpy.zeros(l-2)
    y_temp = numpy.zeros(l-2)

    for i in range(1,l-1):
        x_temp[i-1] = x[i]

        dy = (y[i] - y[i-1] + y[i+1] - y[i]) / 2

        y_temp[i-1] = dy / dx

    return x_temp, y_temp    
    
# INTERPOLATION  

def interpolate_data(original_x, original_y, new_x, interpolate_kind = "default", verbose = 0):
    """
    Interpolate data 
    
    kind = Specifies the kind of interpolation as a string ('linear', 'nearest', 'zero', 'slinear', 'quadratic, 'cubic', where 'slinear', 'quadratic' and 'cubic' refer to a spline interpolation of first, second or third order) or as an integer specifying the order of the spline interpolator to use. Default is 'linear'
    """    
    
    if interpolate_kind == "default":
        interpolate_kind = "linear"
    
    # DEBUG.verbose("  Interpolating data using %s" % (interpolate_kind), verbose_level = 1)
    
    f = interp1d(original_x, original_y, kind = interpolate_kind)
    new_y = f(new_x)    

    return new_y




def interpolate_two_datasets(x1, y1, x2, y2, x_step = 1, interpolation_kind = "default", verbose = 0):
    """
    Take datasets 1 and 2 and unify the x-axis, interpolate the y-values of both for the new axis. The new x-axis will be only where x1 and x2 overlap. 
    
    INPUTS:
    x1, x2 (ndarray, list): x-axes of the data
    y1, y2 (ndarray, list): y values of the data
    x_step (number): step size of the x-axis of the interpolated data
    interpolation_kind (string): Specifies the kind of interpolation as a string ('linear', 'nearest', 'zero', 'slinear', 'quadratic, 'cubic', where 'slinear', 'quadratic' and 'cubic' refer to a spline interpolation of first, second or third order) or as an integer specifying the order of the spline interpolator to use. Default is 'linear'
    
    OUTPUTS:
    new_x (ndarray): new x-axis
    new_y1, new_y2 (ndarray): the interpolated values of y1 and y2
    
    
    """
    
    if interpolation_kind == "default":
        interpolation_kind = "linear"
        
        
    x1 = CF.make_numpy_ndarray(x1)
    y1 = CF.make_numpy_ndarray(y1)
    x2 = CF.make_numpy_ndarray(x2)
    y2 = CF.make_numpy_ndarray(y2)
    
    if x1[0] > x1[-1]:
        x1 = x1[::-1]
        y1 = y1[::-1]

    if x2[0] > x2[-1]:
        x2 = x2[::-1]
        y2 = y2[::-1]
    
    
    if x1[0] > x2[0]:
        start = x1[0]
    else:
        start = x2[0]
        
    if x1[-1] < x2[-1]:
        finish = x1[-1]
    else:
        finish = x2[-1]    
        
    if verbose > 0:
        print(start, finish)

    new_x = numpy.arange(start, finish, step = x_step)

    f = interp1d(x1, y1, kind = interpolation_kind)
    new_y1 = f(new_x)
    
    f = interp1d(x2, y2, kind = interpolation_kind)
    new_y2 = f(new_x)
    
    return new_x, new_y1, new_y2













