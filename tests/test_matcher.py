import unittest
from your_module import fuzzy_match  # Replace 'your_module' with the actual module where the fuzzy_match function is defined

class TestFuzzyMatcher(unittest.TestCase):

    def test_exact_match(self):
        self.assertTrue(fuzzy_match("hello", "hello"))

    def test_partial_match(self):
        self.assertTrue(fuzzy_match("hello", "hell"))

    def test_no_match(self):
        self.assertFalse(fuzzy_match("hello", "world"))

    def test_case_insensitivity(self):
        self.assertTrue(fuzzy_match("Hello", "hello"))

    def test_fuzzy_match_with_threshold(self):
        self.assertTrue(fuzzy_match("hello", "hallo", threshold=0.8))  # Adjust threshold as needed

    def test_empty_string(self):
        self.assertFalse(fuzzy_match("", "hello"))
        self.assertFalse(fuzzy_match("hello", ""))

if __name__ == '__main__':
    unittest.main()