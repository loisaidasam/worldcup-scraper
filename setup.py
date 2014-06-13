
from distutils.core import setup

from scraper import __version__

setup(
    name="worldcupscraper",
    version=__version__,
    description="A Python scraper for World Cup soccer data",
    author="@LoisaidaSam",
    author_email="sam.sandberg@gmail.com",
    packages=["scraper"],
    install_requires=["requests","bs4"],
)
