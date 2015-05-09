#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, web

items = {'movies': 'm', 'tvResults': 'tv', 'actors': 'celebrity'}

def getThumbnail(id, url, type):
    import urllib
    import os.path

    if url.endswith('gif'):
        return 'images/%s.png' % type

    newImagePath = '%s/%s' % (wf.cachedir, id)

    if not os.path.isfile(newImagePath):
        urllib.urlretrieve(url, newImagePath)

    return newImagePath


def main(wf):
    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    url = 'http://www.rottentomatoes.com/search/json/'
    params = dict(q_enc='UTF-8',
                  catCount=2,
                  q=query.strip())

    response = web.get(url, params)
    json = response.json()

    for key in items.keys():
        for item in json[key]:
            title = item['name']
            subtitle = ''
            id = '%s' % item['vanity']
            # ico = getThumbnail(id, item['image'], key)
            url = 'http://www.rottentomatoes.com/%s/%s' % (items[key], id)

            if 'subline' in item:
                subtitle = item['subline']

            if 'year' in item:
                title = u'%s (%s)' % (title, item['year'])

            if 'startYear' in item and 'endYear' in item:
                title = u'%s (%s - %s)' % (title, item['startYear'], item['endYear'])

            wf.add_item(
                title=title,
                subtitle=subtitle,
                arg=url,
                valid=True,
                icon='images/%s.png' % key,
                icontype=None,
                uid=id
            )

    wf.send_feedback()


if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))