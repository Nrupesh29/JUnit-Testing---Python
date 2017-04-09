'''
A test suite is a list of tests. 
Each test is a tuple of 3 elements:
functionn: a function object
parameters: a list of parameters to the function
expected: the expected return value
'''

template = ('function', 'parameters', 'expected')
FUNCTION = 0
PARAMETERS = 1
EXPECTED = 2

def correct_test_format(test):
    '''
    Returns True if parameter is a correctly formatted test case.
    '''
    return isinstance(test, tuple) and len(test) == len(template) and \
            isinstance(test[PARAMETERS], list) and callable(test[FUNCTION])


def correct_suite_format(suite):
    '''
    Returns True if parameter is a correctly formatted test suite. The parameter must be a list, and each element must be a correctly formatted test case.
    '''
    if isinstance(suite, list):
        for test in suite:
            if not correct_test_format(test):
                return False
        return True
    return False


def run_test(test):
    '''
    Return True if test passes, False if test is not correctly formatted or does not return expected value
    '''
    return correct_test_format(test) and (test[FUNCTION](*test[PARAMETERS]) == test[EXPECTED])


def run_suite(suite):
    '''
    Run list of tests and return a list of [number of tests passed, number of tests failed]
    '''
    RESULT = [0, 0]
    PASSED = 0
    FAILED = 1

    if not correct_suite_format(suite):
        return RESULT
    for test in suite:
        if run_test(test):
            RESULT[PASSED] += 1
        else:
            RESULT[FAILED] += 1

    return RESULT
