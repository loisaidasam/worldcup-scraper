#!/usr/bin/env python

import json

from bs4 import BeautifulSoup
import requests


__version__ = '0.0.1'


def scrape():
    html = requests.get('http://www.livescore.com/worldcup/').content
    soup = BeautifulSoup(html)
    match = soup.find(class_='match')
    time = match.find(class_='fd').text.strip()
    team_home = match.find(class_='tl').text.strip()
    team_away = match.find(class_='tr').text.strip()
    score_pieces = match.find(class_='fs').text.strip().split()
    return {
        'time': time,
        'teams': [
            {
                'team': team_home,
                'score': score_pieces[0],
            },
            {
                'team': team_away,
                'score': score_pieces[2],
            },
        ],
    }


def main():
    print json.dumps(scrape())


if __name__ == '__main__':
    main()
