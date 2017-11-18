import json
import os
import unittest

from riverfordScraper import cabbageCheck, parser


class TestScraper(unittest.TestCase):
    def setUp(self):
        self.allowedBoxes = ["Large veg box (less roots)",
                             "Large veg box",
                             "Bumper veg box (original)"]

        with open(os.path.join(os.path.dirname(__file__),
                               "data/scrapedHtml.html"), "r") as f:
            self.testHtml = f.read()

        with open(os.path.join(os.path.dirname(__file__),
                               "data/boxContents.json"), "r") as f:
            self.sampleBoxContents = json.load(f)

    def testParser(self):
        output = parser.parseBoxContentsPage(self.testHtml)
        self.assertEqual(self.sampleBoxContents, output,
                         "Wrong box contents extracted")

    def testContainsCabbage(self):
        self.assertFalse(cabbageCheck.containsCababage(
                        self.sampleBoxContents["Juicing box"]),
                        "Found invisible cabbage")

        self.assertTrue(cabbageCheck.containsCababage(
                        self.sampleBoxContents["Bumper veg box (original)"]),
                        "Failed to spot cabbage")

    def testfindAlternativeBoxes(self):
        self.assertEqual(cabbageCheck.findAlternativeBoxes(
                                                    self.sampleBoxContents,
                                                    self.allowedBoxes),
                         [])
        self.assertEqual(cabbageCheck.findAlternativeBoxes(
                                                    self.sampleBoxContents,
                                                    ["Salad box",
                                                     "100% UK veg box"]),
                         ["Salad box"])


if __name__ == '__main__':
    unittest.main()
