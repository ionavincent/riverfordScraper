import config
import json

import requests


def sendSlackNotification(text):
    slack_data = {'text': "%s" % text}

    response = requests.post(
        config.slackUrl, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code != 200:
        raise ValueError(
            'Request to slack returned an error %s, the response is:\n%s'
            % (response.status_code, response.text)
        )
