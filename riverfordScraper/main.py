import parser

import cabbageCheck
from scraper import Scraper

URL = "https://www.riverford.co.uk/box-contents"
PREFERRED_BOX = "Large veg box (less roots)"
ALLOWED_BOXES = ["Large veg box (less roots)",
                 "Large veg box",
                 "Bumper veg box (original)"]


def main():
    scraper = Scraper(cache_name=__name__, cache_expiry=36000)
    scrapedHtml = scraper.get(url=URL)

    allBoxesInfo = parser.parseBoxContentsPage(scrapedHtml)
    if cabbageCheck.containsCababage(allBoxesInfo[PREFERRED_BOX]):
        altBoxes = cabbageCheck.findAlternativeBoxes(allBoxesInfo,
                                                     ALLOWED_BOXES)
        if len(altBoxes):
            print ("Your preferred box has cabbage in it this week. "
                   "But fear not, there are "
                   "cabbage free alternatives: %s" % ', '.join(altBoxes))
        else:
            print "Alas, all the boxes you buy contain cabbage this week"
    else:
        print "You are free from cabbage this week"


if __name__ == '__main__':
    main()

# TODO: Add slack notifications
# TODO: Add config file
