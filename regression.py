import sys
import unittest

if __name__ == '__main__':
    result = None
    suite: unittest.TestSuite = unittest.TestLoader().discover(".", "*.py")
    testResult = unittest.TestResult()
    result = suite.run(testResult,  'Full')
    sys.exit(result)

