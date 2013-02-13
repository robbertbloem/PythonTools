PYTHONTOOLS

A collection of functions that I seem to use for every python project.


0 - DISCLAIMER
There is no warranty on this code. For bugs, please email me: info at robbert dot org


1 - THANKS
The code is heavily influenced by examples from the internet. Thanks to the Python community!


2 - INSTALLATION/SETUP:

- make sure you have Numpy, Scipy, Matplotlib and ipython installed. This is done most conveniently using the "Enthought Python Distribution" (Google it). There is a full version with academic license. It also works with the free version. There are versions for Windows, Mac and Linux. 
- copy everything to a convenient place
- add that place to the PYTHONPATH in for example .bash_profile: 
export PYTHONPATH=$HOME/Developer:$HOME/path_to_pythontools/PythonTools:$PYTHONPATH 


3 - ORGANIZATION

3.1 - CLASSTOOLS

ClassTools contain some very general methods: 
- a method to write the contents of a class as pretty output
- shortcuts to the debug methods: verbose, printWarning and printError


3.2 - DEBUG

- verbose(string, flag_verbose = False): print a string if flag_verbose == True. If it is false, it will not print stuff :) The "if" is in the function to clean up the code. The text has a blue color.
- printWarning(string, location), printError(string, location): will print a string when called. "location" is given by inspect.stack(). printWarning is used for an exception after which the code continues, printError is for exceptions where the code will not continue (for example: wrong filename).


3.3 - OBJECTARRAY
 
To complicated for the late evening



3.4 - RELOADALL



3.5 - TESTS

Most modules come with tests to ensure:
- that a function works correctly with the correct input
- that a functions elegantly handles edge-cases and incorrect input
- to ensure that the behavior of functions does not change when functions are modified. 
Test should be made for the smallest possible functions, from the start. The tests describes the behavior of the function: what to do when the input is this or that. 
In general, tests should only be added. When test are removed or changed the behavior may change, leading to errors elsewhere.
To put it differently: changing tests is usually not the correct way to fix a test that gives an error. 
Read more about test driven development: https://en.wikipedia.org/wiki/Test-driven_development

















