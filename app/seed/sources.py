
class Source:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topics(self, topics):
        self.topics.extend(topics)

class CNBC(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('CNBC')
        self.url = 'https://www.cnbc.com/rss-feeds/'
        self.add_topics(list(set(topics)))


class SeekingAlpha(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Seeking Alpha')
        self.url = 'https://seekingalpha.com/feed.xml'
        self.field_map = {
            'title': 'title',
            'date': 'published',
            'link': 'link'
        }

        self.add_topics(list(set(topics)))


class Investing(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Investing.com')
        self.url = 'https://www.investing.com/rss/news_25.rss'
        self.add_topics(list(set(topics)))

class Nasdaq(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Nasdaq')
        self.url = 'https://www.nasdaq.com/feed/rssoutbound?category=Stocks'
        self.add_topics(list(set(topics)))

class WSJ(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('WSJ')

        self.add_topics(list(set(topics)))


class Yahoo(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Yahoo Finance')

        self.add_topics(list(set(topics)))


class FT(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('FT')

        self.add_topics(list(set(topics)))


class Fortune(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Fortune')
        self.add_topics(list(set(topics)))


class MarketWatch(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('MarketWatch')

        self.add_topics(list(set(topics)))


class Zacks(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Zacks')

        self.add_topics(list(set(topics)))


class Reddit(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Reddit')
        self.add_topics(list(set(topics)))


class CNNMoney(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('CNN Money')
        self.add_topics(list(set(topics)))


class Reuters(Source):
    def __init__(self, topics=None):
        if topics is None:
            topics = []
        super().__init__('Reuters')
        self.add_topics(list(set(topics)))



class SourceSeeder:

    @staticmethod
    def create_source(source_class, topics):
        return source_class(topics=topics)

    @staticmethod
    def generate_sources(sources):
        # Here you could save your source objects to a database
        for source in sources:
            print(f'Saving source: {source.name} with topics: {source.topics}')

    @classmethod
    def seed_sources(cls, source_classes, topics):
        sources = [cls.create_source(source_class, topics) for source_class in source_classes]
        cls.generate_sources(sources)
