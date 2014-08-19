#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, web

CONSUMER_KEY = '10d6d72dff73e61540286435167eb274'

def main(wf):

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    url = 'https://api.4shared.com/v0/files.json'
    params = dict(oauth_consumer_key = CONSUMER_KEY,
                  query = query.strip(),
                  category = 1,
                  offset = 0,
                  limit = 10)

    response = web.get(url, params)
    for item in response.json()['files']:
        wf.add_item(
            title = item['name'],
            subtitle = "{0:.2f}MB".format(item['size'] / 1024.0 / 1024.0),
            arg = item['downloadPage'],
            valid = True,
            uid = item['id']
        )

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))