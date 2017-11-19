# RiverfordScraper
A website scraper to check Riverford vegetable box contents and send a slack
message of the results.

It checks the contents of your preferred box, and if that contains a given
vegetable, say cabbage, goes on to check whether any other permitted boxes do
not, and sends a slack message to let you know what will be coming, or suggest
an alternative box.

It requires the following environment variables to be set:

`UNWANTED_VEGETABLE`: The name of the vegetable you wish to avoid
`PREFERRED_BOX`: The name of your preferred box, as it appears [here](https://www.riverford.co.uk/box-contents)
`ALLOWED_BOXES`: A comma separated list of all permitted box names, as they
appear [here](https://www.riverford.co.uk/box-contents)

`SLACK_URL`: The slack web hook url