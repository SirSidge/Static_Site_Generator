import unittest

from main import extract_title

class MainTestRun(unittest.TestCase):
    def test_markdown_header(self): #Needs the word "test" at the start of the function name "test_markdown_header"
        header = "# Hello"
        self.assertEqual(extract_title(header), "Hello")
        header = "* Hello"
        with self.assertRaises(Exception):
            extract_title(header)