from .collector import Collector
from config import Config

class CounsilInsights(Collector):

    def __init__(self):
        super().__init__()
        config = Config().get('collector').get('council-insights')
        self.start_id = config.get('start_id')
        self.end_id = config.get('end_id')
        self.base_url = config.get('base_url')

    def process(self):
        for asset in self.get_assets():
            asset = self.transform(asset)
            self.save_asset(asset)

    def transform(self, asset):
        """ overload function from parent"""
        # do something specific
        return asset
