

import asyncio
import FinNews as fn

import FinNews as fn

from app.services.rss.rss import RSSFeed
from app.services.rss.source import SeekingAlpha


def main():

    rss = RSSFeed()

    source = SeekingAlpha()

    
    source_entries = rss.fetch_feed_entries(source, 5)

    for entry in source_entries:
        print(entry.title)
        print(entry.url)
        print(entry.date)
        print('------------------')


main()
