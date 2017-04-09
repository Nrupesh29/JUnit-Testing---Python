import unittest
from part1 import *


class TestFnTester(unittest.TestCase):

    """
    Test Cases for correct_test_format() function from PART1
    """
    def test_correct_format_for_test_case(self):
        """
        Testing a Test Case for Correct format
        """
        self.assertTrue(correct_test_format((len, ['hello'], 5)))

    def test_parameter_not_tuple(self):
        """
        Testing a Test Case when it is not a tuple
        """
        self.assertFalse(correct_test_format([(len, ['hello'], 5)]))

    def test_parameter_not_of_length_3(self):
        """
        Testing a Test Case which is not a tuple of length 3
        """
        self.assertFalse(correct_test_format((len, ['hello'], 3, False)))

    def test_first_element_not_a_function(self):
        """
        Testing a Test Case when first element of tuple is not a function
        """
        self.assertFalse(correct_test_format(('add', [1, 2], 3)))

    def test_second_element_not_a_list(self):
        """
        Testing a Test Case when second element of tuple is not a list
        """
        self.assertFalse(correct_test_format((type, 'hello', str)))


    """
    Test Cases for correct_suite_format() function from PART1
    """
    def test_correct_format_for_test_suite(self):
        """
        Testing a Test Suite for Correct format
        """
        self.assertTrue(correct_suite_format([(len, ['hello'], 5), (type, ['hello'], str), (abs, [-2], 2)]))

    def test_parameter_not_list(self):
        """
        Testing a Test Suite when it is not a list
        """
        self.assertFalse(correct_suite_format((abs, [-2], 2)))

    def test_one_test_case_invalid_format(self):
        """
        Testing a Test Suite when at least one test case is not in valid format
        """
        self.assertFalse(correct_suite_format([(len, ['hello'], 5), (type, ['hello'], str), (abs, -2, 2)]))


    """
    Test Cases for run_test() function from PART1
    """
    def test_correct_format_and_valid_return_value(self):
        """
        Testing a Test Case for Correct format and valid return value
        """
        self.assertTrue(run_test((abs, [-2], 2)))

    def test_correct_format_and_invalid_return_value(self):
        """
        Testing a Test Case for Correct format and invalid return value
        """
        self.assertFalse(run_test((type, ['hello'], int)))

    def test_correct_format_and_exception_raised(self):
        """
        Testing a Test Case for Correct format and exception instead of return value
        """
        self.assertRaises(Exception, run_test, (abs, ['Hello'], 2))

    def test_parameter_not_in_correct_format(self):
        """
        Testing a Test Case with invalid format
        """
        self.assertFalse(run_test((abs, -2, 2)))
    

    """
    Test Cases for run_suite() function from PART1
    """
    def test_correct_format_and_pass_not_equal_to_fail(self):
        """
        Testing a Test Suite for correct format and number of pass tests not equal to number of failed tests
        """
        self.assertNotEqual(run_suite([(len, ['hello'], 2), (type, ['hello'], str), (abs, [-2], 2)]), [0, 0])
        self.assertNotEqual(run_suite([(len, ['hello'], 2), (type, ['hello'], str), (abs, [-2], 2)])[0], run_suite([(len, ['hello'], 2), (type, ['hello'], str), (abs, [-2], 2)])[1])

    def test_parameter_invalid_format(self):
        """
        Testing a Test Suite for invalid format
        """
        self.assertEqual(run_suite([(len, 'hello', 2), (type, ['hello'], str), (abs, [-2], 2)]), [0, 0])


if __name__ == "__main__":
    unittest.main()
