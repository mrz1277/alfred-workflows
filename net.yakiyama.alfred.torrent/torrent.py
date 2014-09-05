# -*- coding: utf-8 -*-

import sys
from ConfigParser import SafeConfigParser
from workflow import Workflow


def main(wf):
    import requests
    from bs4 import BeautifulSoup as Soup

    if len(wf.args):
        query = wf.args[0]
    else:
        query = None

    parser = SafeConfigParser()
    parser.read('config.cfg')

    utorrent_gui = parser.get('uTorrent', 'gui_address')
    username = parser.get('uTorrent', 'gui_username')
    password = parser.get('uTorrent', 'gui_password')

    # Use the same session to retrieve the token and make the api call
    s = requests.Session()

    # Get token
    token_request = s.get(utorrent_gui+"/token.html", auth=(username, password))
    token_soup = Soup(token_request.text)
    div = token_soup.find("div")
    token = div.text

    # Call uTorrent web api to start download
    torrent_url = query
    api_url = utorrent_gui+"/?action=add-url"+"&token="+token+"&s="+torrent_url
    r = s.get(api_url, auth=(username, password))

    if r.status_code == 200:
        print "다운로드를 시작합니다."
    else:
        print "오류가 발생했습니다."

if __name__ == u"__main__":
    wf = Workflow(libraries=['./lib'])
    sys.exit(wf.run(main))
