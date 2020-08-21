#!/usr/bin/env python3
"""
Unit Test cases for wordcount

Students should not modify this file.
"""

import sys
import unittest
import importlib
import subprocess
from contextlib import redirect_stdout
from io import StringIO

# Kenzie devs: change this to 'soln.wordcount' to test solution
PKG_NAME = 'wordcount'

small_dict = {
    '--': 1, 'are': 3, 'at': 1, 'be': 3,
    'but': 1, 'coach': 1, 'football': 1,
    'least': 1, 'need': 1, 'not': 3, 'should': 1,
    'to': 2, 'used': 1, 'we': 6, 'what': 3
    }

alice_top_20 = [
    '1605', '766', '706', '614', '518', '493', '421', '362',
    '352', '333', '265', '261', '249', '222', '221', '208',
    '206', '176', '169', '155'
    ]


class TestWordcount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Performs module import and suite setup at test-runtime"""
        # check for python3
        cls.assertGreaterEqual(cls, sys.version_info[0], 3)
        # This will import the module to be tested
        cls.module = importlib.import_module(PKG_NAME)

    def test_print_words(self):
        """Check the console output from print_words()"""
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.print_words("books/alice.txt")
            output = buffer.getvalue().splitlines()
        self.assertEqual(len(output), 4950)

    def test_print_top(self):
        """Check the console output from print_topcount()"""
        buffer = StringIO()
        with redirect_stdout(buffer):
            self.module.print_top("books/alice.txt")
            output = buffer.getvalue().splitlines()
        self.assertIsInstance(output, list)
        self.assertGreaterEqual(len(output), 20)
        self.assertLess(len(output), 25)
        for count in alice_top_20:
            self.assertIn(count, str(output))

    def test_create_word_dict(self):
        """Check if correct dict is generated"""
        filename = "books/small.txt"
        d = self.module.create_word_dict(filename)
        self.assertIsInstance(d, dict)
        self.assertDictEqual(d, small_dict)

        filename = "books/alice.txt"
        d = self.module.create_word_dict(filename)
        self.assertEqual(len(d), 4950)

    def test_frankenstein(self):
        """Check if Frankenstein book can be counted"""
        filename = "books/good/Frankenstein.txt"
        d = self.module.create_word_dict(filename)
        self.assertEqual(len(d), 11724)

    def test_taletwocities(self):
        """Check if TaleTwoCities book can be counted"""
        filename = "books/good/TaleTwoCities.txt"
        d = self.module.create_word_dict(filename)
        self.assertEqual(len(d), 18620)

    def test_flake8(self):
        """Checking for PEP8/flake8 compliance"""
        result = subprocess.run(['flake8', self.module.__file__])
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
