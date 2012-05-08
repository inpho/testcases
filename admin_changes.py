import unittest2
import autotest
from collections import namedtuple

# set up test suite for running tests
tests = unittest2.defaultTestLoader.getTestCaseNames(autotest.Autotest)
result = unittest2.TestResult()
past_fails = 0
checked = []

# set up string parsing for docstring
testcases = []
count = len(tests)
Test_info = namedtuple('title', ['title', 'description'], verbose=False)

for test in tests:
    testname = 'autotest.Autotest.' + test
    # puts docstring in variable doc
    exec ('doc = ' + testname + '.__doc__')

    # Begin docstring parsing
    # eliminate beginning junk in string
    state = "t"
    t, d = "", ""
    doc = doc[8:]
    for char in doc:
        if state == "t":
            if char == '\n':
                state = "space"
                continue
            else:
                t += char
        elif state == "space":
            if char != " ":
                state = "d"
            else:
                continue
        else:
            if char != "\n":
                d += char
            else:
                case = Test_info(t, d)
                testcases.append(case)

    # Run test
    suite = unittest2.defaultTestLoader.loadTestsFromName(testname)
    suite.run(result)
    current_fails = len(result.errors) + len(result.failures)
    if past_fails == current_fails:
        checked.append(t)
    else:
        past_fails = current_fails

print "TESTCASES:"
for test in testcases:
    print test.title + ": " + test.description 

print "\n\nCHECKED:"
for test in checked:
    print test
