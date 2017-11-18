from bs4 import BeautifulSoup


def parseBoxContentsPage(scrapedHtml):
    """Parses scraped HTML of the box contents page and returns the
    contents of each box"""
    soup = BeautifulSoup(scrapedHtml, "html.parser")
    allBoxesInfo = soup.find_all("div", {"class": "bs-three bs-columns"})

    boxContents = {}

    for boxInfo in allBoxesInfo:
        titleString = boxInfo.find('a').text.strip()
        contents = [item.text for item in boxInfo.find_all('li')]
        boxContents[titleString] = contents

    import json
    with open("/Users/ivincent/boxContents.json", "w+") as f:
        f.write(json.dumps(boxContents, indent=4, sort_keys=True))
    return boxContents
