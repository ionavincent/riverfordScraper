import parser
import sched

import cabbageCheck
import config
import notifier
from scraper import Scraper


def main():
    scraper = Scraper(cache_name=__name__, cache_expiry=36000)
    scrapedHtml = scraper.get(url=config.riverfordUrl)

    allBoxesInfo = parser.parseBoxContentsPage(scrapedHtml)

    message = getMessage(allBoxesInfo)
    if message:
        notifier.sendSlackNotification(message)


def getMessage(allBoxesInfo):
    if cabbageCheck.containsCababage(allBoxesInfo[config.preferredBox]):
        altBoxes = cabbageCheck.findAlternativeBoxes(allBoxesInfo,
                                                     config.allowedBoxes)
        if len(altBoxes):
            return ("Your preferred box has cabbage in it this week. "
                   "But fear not, there are "
                   "cabbage free alternatives: %s" % ', '.join(altBoxes))
        else:
            return ("Alas, all the boxes you buy contain cabbage this week. "
                    "Bad luck.")
    else:
        return "You are free from cabbage this week"


if __name__ == '__main__':
    main()

# TODO: Add config file
