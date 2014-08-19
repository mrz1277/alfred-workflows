#!/usr/bin/python
# encoding: utf-8

import sys

from workflow import Workflow, web

def getThumbnail(id, url, type):

    import urllib
    import os.path

    if len(url) == 0:
        return '%s.png' % type

    extension = 'png' if url.endswith('png') else 'jpg'
    newImagePath = '%s/%s.%s' % (wf.cachedir, id, extension)

    if not os.path.isfile(newImagePath):
        minifiedImageUrl = '%s?type=%s' % (url, 'n30_43_2')
        urllib.urlretrieve(minifiedImageUrl, newImagePath)

    return newImagePath

def main(wf):

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    url = 'http://auto.movie.naver.com/ac'
    params = dict(q_enc = 'UTF-8',
                  st = 1,
                  r_lt = 1,
                  n_ext = 1,
                  t_koreng = 1,
                  r_format = 'json',
                  r_enc = 'UTF-8',
                  r_unicode = 0,
                  r_escape = 1,
                  q = query.strip())

    response = web.get(url, params)
    for items in response.json()['items']:
        for item in items:

            if len(item) < 7:
                continue

            title = item[0][0]
            date = item[1][0]
            subtitle = item[2][0]
            thumb = item[3][0]
            unknown = item[4][0]
            id = item[5][0]
            resultType = item[6][0]
            ico = getThumbnail(id, thumb, resultType)
            url = 'http://movie.naver.com/movie/bi/mi/basic.nhn?code=%s' % id

            if len(date) >= 4:
                title = u'%s (%s)' % (title, date[:4])

            if (resultType == u'people'):
                url = url.replace('mi', 'pi')

            wf.add_item(
                title = title,
                subtitle = subtitle,
                arg = url,
                valid = True,
                icon = ico,
                icontype = None,
                uid = id
            )

    wf.send_feedback()

if __name__ == '__main__':
    wf = Workflow()
    sys.exit(wf.run(main))