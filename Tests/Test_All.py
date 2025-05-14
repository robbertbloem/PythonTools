import importlib

import unittest

import PythonTools.Tests.ClassTools_Tests
import PythonTools.Tests.CommonFunctions_Tests
import PythonTools.Tests.Constants_Tests
import PythonTools.Tests.Equations_Tests
import PythonTools.Tests.Mathematics_Tests
import PythonTools.Tests.PlottingTools_Tests

importlib.reload(PythonTools.Tests.ClassTools_Tests)
importlib.reload(PythonTools.Tests.CommonFunctions_Tests)
importlib.reload(PythonTools.Tests.Constants_Tests)
importlib.reload(PythonTools.Tests.Equations_Tests)
importlib.reload(PythonTools.Tests.Mathematics_Tests)
importlib.reload(PythonTools.Tests.PlottingTools_Tests)

verbosity = 2

TS = unittest.TestSuite()

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.ClassTools_Tests)
TS.addTests(tests)

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.CommonFunctions_Tests)
TS.addTests(tests)

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.Constants_Tests)
TS.addTests(tests)

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.Equations_Tests)
TS.addTests(tests)

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.Mathematics_Tests)
TS.addTests(tests)

TL = unittest.TestLoader()
tests = TL.loadTestsFromModule(PythonTools.Tests.PlottingTools_Tests)
TS.addTests(tests)

result = unittest.TestResult()
TS.run(result)

print(result)