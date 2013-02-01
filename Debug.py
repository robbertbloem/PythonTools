from __future__ import print_function
from __future__ import division

def printError(string, location = []):
    """
    printError: print an error in red.

    20130103/RB: copied the function from croc
    20130131/RB: copied to Crocodile

    INPUT:
    - string (str): an error message
    - location (inspect.stack(), opt): makes tracing the location of the error easier.

    """   
    if location == []:
        print("\033[1;31mERROR: " + string + "\033[1;m")
    else:
        print("\033[1;31mERROR (" + location[0][1] + ":" + location[0][3] + ":" + str(location[0][2]) + "): " + string + "\033[1;m")


def printWarning(string, location = []):
    """
    printWarning: print a warning in purple.

    20130103/RB: copied the function from croc
    20130131/RB: copied to Crocodile

    INPUT:
    - string (str): a warning message
    - location (inspect.stack(), opt): makes tracing the location of the warning easier.

    """   
    if location == []:
        print("\033[1;35mWARNING: " + string + "\033[1;m")
    else:
        # print("\033[1;35mWARNING (" + location[0][1] + "): " + string + "\033[1;m")
        print("\033[1;35mWARNING (" + location[0][1] + ":" + location[0][3] + ":" + str(location[0][2]) + "): " + string + "\033[1;m")


def verbose(string, flag_verbose):
    """
    verbose: talk about the progress, in blue

    20130103/RB: started the function
    20130131/RB: copied to Crocodile

    INPUT:
    - string (str): a message
    - flag_verbose (BOOL): if False, don't print anything.

    REMARK:
    I was tired if all if-statements in the code, so I moved it in here.

    """ 
    if flag_verbose:
        print("\033[1;34m" + string + "\033[1;m")
