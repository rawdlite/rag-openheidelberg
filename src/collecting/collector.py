from couchdbclient import Client
from config import Config

class Collector:

    def __init__(self)-> None:
        self.config = Config().get('collector')
        self.client = Client()


    def get_assets(self) -> list:
        pass

    def transform(self, doc: dict) -> dict:
        return doc

    def save_asset(self, doc: dict) -> dict:
        self.client.db.put(doc)
        return doc
