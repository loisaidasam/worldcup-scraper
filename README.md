worldcup-scraper
================

Scraper for getting live World Cup data

## Installation

    $ git clone git@github.com:loisaidasam/worldcup-scraper.git
    $ cd worldcup-scraper
    $ pip install -r requirements.txt

## Usage

    >>> from scraper import scrape
    >>> scrape()
    {'teams': [{'score': u'3', 'team': u'Brazil'},
      {'score': u'1', 'team': u'Croatia'}],
    'time': u'FT'}

Pretty easy huh?
