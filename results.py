import unittest2
import autotest

tests = unittest2.defaultTestLoader.getTestCaseNames(autotest.Autotest)
result = unittest2.TestResult()
failed = 0

for test in tests:
    testname = 'autotest.Autotest.' + test
    exec ('doc = ' + testname + '.__doc__')
    suite = unittest2.defaultTestLoader.loadTestsFromName(testname)
    suite.run(result)
    fails = len(result.errors) + len(result.failures)
    if failed < fails:
        print ("FAILED: " + doc + "\n\n")
        print ("-----------------------------------------------\n")
        failed = fails
    else:
        print ("PASSED: " + doc + "\n")
        print ("-----------------------------------------------\n\n")
        

#suite = unittest2.TestLoader().loadTestsFromTestCase(autotest.Autotest)
#result = unittest2.TextTestRunner(verbosity=2).run(suite)


#print result.errors
#print len(result.errors)

#print result.failures
#print len(result.failures)

