# -*- coding: utf-8 -*-

import sys
from workflow import Workflow, web


def main(wf):
    from bs4 import BeautifulSoup as Soup

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    r = web.get(query)
    soup = Soup(r.text)
    donwload_links = soup.find_all("td", "view_file")
    magnet = donwload_links[-1]
    href = magnet.find('a')['href']
    simple_href = href.split('&')[0]

    print str(simple_href)

if __name__ == u"__main__":
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
