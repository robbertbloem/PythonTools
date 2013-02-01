PYTHONTOOLS

A collection of functions that I seem to use for every python project.

0 - DISCLAIMER
There is no warranty on this code. For bugs, please email me: info at robbert dot org

1 - THANKS
The code is heavily influenced by examples from the internet. Thanks to the Python community!


2 - ORGANIZATION
ClassTools contain some very general methods: 
- a method to write the contents of a class as pretty output
- shortcuts to the debug methods: verbose, printWarning and printError

Debug:
- verbose(string, flag_verbose = False): print a string if flag_verbose == True. If it is false, it will not print stuff :) The "if" is in the function to clean up the code. The text has a blue color.
- printWarning(string, location), printError(string, location): will print a string when called. "location" is given by inspect.stack(). printWarning is used for an exception after which the code continues, printError is for exceptions where the code will not continue (for example: wrong filename).

ObjectArray: 
To complicated for the late evening