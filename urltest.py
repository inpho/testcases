
##  Example code of how to run tests and access them outside of
##  autotest.py and access the list of passed tests.

import autotest

if __name__ == '__main__':
    suite = autotest.unittest2.TestLoader().loadTestsFromTestCase(autotest.Autotest)
    autotest.unittest2.TextTestRunner(verbosity=2).run(suite)
    print autotest.passed
