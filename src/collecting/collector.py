import couchdb2

class Collector:

    def __init__(self)-> None:
        self.config = Config()


    def get_assets(self) -> list:
        pass

    def transform(self, doc: dict) -> dict:
        return doc

    def save_asset(self, doc: dict) -> dict:
        return doc
