# Unit-Testing-Python

### Part I

The functions work on a list of test cases (Refer to the whole list as a test suite).

Each test case is a tuple of 3 elements

  - the function to call
  - the list of parameters to pass to the function
  - the expected result

The functions:

- correct_test_format(test)
  - Returns True if parameter is a correctly formatted test case.
  - To check the tuple and list types, use isinstance(obj, type) – try this out in the interpreter
  - To check if the function argument has the right type, use callable(obj). For example, callable(print) returns True.

- correct_suite_format(suite)
  - Returns True if parameter is a correctly formatted test suite. The parameter must be a list, and each element must be a correctly formatted test case.

- run_test(test)
  - Return True if test passes, False if test is not correctly formatted or does not return expected value

- run_suite(suite)
  - Run list of tests and return a list of [number of tests passed, number of tests failed]

### Part II

Tests the functions from part1:

- For correct_test_format(), you have 5 test cases:
  - correct format
  - parameter is not a tuple
  - parameter is not of length 3
  - parameter’s first element is not a function
  - parameter’s 2nd element is not a list

- For correct_suite_format(), you have 3 test cases:
  - correct format
  - parameter is not a list
  - parameter is a list, but at least one test case is not of the correct format

- For run_test(), you have 4 test cases:
  - parameter is of correct format and returns expected value
  - parameter is of correct format, but does not return expected value
  - parameter is of correct format, but instead of returning a value, it throws an exception (this was not required for hw1)
  - note that if you run this test on your hw1 solution, it will probably fail. In the spirit of test-driven development, you     don’t have to modify the code to get this to pass. (Treat it like it’s the test for the next iteration to implement.)
  - parameter is not of correct format

- For run_suite(), you have 2 cases
  - parameter is of correct format and includes at least one pass and one failure (but not the same number of passes as           failures)
  - parameter is not of correct format
