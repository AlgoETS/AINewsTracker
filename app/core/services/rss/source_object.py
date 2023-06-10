class Source:
    def __init__(self, name):
        self.name = name
        self.topics = []

    def add_topics(self, topics):
        self.topics.extend(topics)
