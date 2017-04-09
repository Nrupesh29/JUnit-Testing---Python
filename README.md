# JUnit-Testing-Python

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
