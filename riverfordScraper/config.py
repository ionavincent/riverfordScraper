import os

riverfordUrl = "https://www.riverford.co.uk/box-contents"
preferredBox = os.environ["PREFERRED_BOX"]
allowedBoxes = os.environ["ALLOWED_BOXES"].split(",")
unwantedVegetable = os.environ["UNWANTED_VEGETABLE"]

slackUrl = os.environ["SLACK_URL"]
