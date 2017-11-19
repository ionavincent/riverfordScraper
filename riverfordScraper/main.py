import config
import parser

import notifier
import vegetableCheck
from scraper import Scraper


def main():
    scraper = Scraper(cache_name=__name__, cache_expiry=36000)
    scrapedHtml = scraper.get(url=config.riverfordUrl)

    allBoxesInfo = parser.parseBoxContentsPage(scrapedHtml)

    message = getMessage(allBoxesInfo)
    if message:
        notifier.sendSlackNotification(message)


def getMessage(allBoxesInfo):
    if vegetableCheck.containsVegetable(config.unwantedVegetable,
                                        allBoxesInfo[config.preferredBox]):
        altBoxes = vegetableCheck.findAlternativeBoxes(
                                                    config.unwantedVegetable,
                                                    allBoxesInfo,
                                                    config.allowedBoxes)
        if len(altBoxes):
            return ("Your preferred box has %s in it this week. "
                    "But fear not, there are "
                    "%s free alternatives: %s" % (config.unwantedVegetable,
                                                  ', '.join(altBoxes)))
        else:
            return ("Alas, *all your box options contain %s* this week. "
                    "Bad luck.\n\n*Contents:*\n%s" % (
                                config.unwantedVegetable,
                                '\n'.join(allBoxesInfo[config.preferredBox])))
    else:
        return ("*You are free from %s this week.*\n\n*Contents:*"
                "\n%s" % (config.unwantedVegetable,
                          '\n'.join(allBoxesInfo[config.preferredBox])))


if __name__ == '__main__':
    main()
