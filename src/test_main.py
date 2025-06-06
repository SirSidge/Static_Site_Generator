import unittest

from main import extract_title

class MainTestRun(unittest.TestCase):
    def markdown_header(self):
        header = "# Heading"
        self.assertEqual(
            extract_title(header),
            "Heading"
        )