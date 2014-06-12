worldcup-scraper
================

Scraper for obtaining live World Cup data. Use at your own risk.

Data sourced from [http://www.livescore.com/worldcup/](http://www.livescore.com/worldcup/)

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
