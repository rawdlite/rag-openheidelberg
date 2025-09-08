from collector import Collector

class CounsilInsights(Collector):

    def __init__(self):
        super().__init__()

    def process(self):
        for asset in self.get_assets():
            asset = self.transform(asset)
            self.save_asset(asset)

    def transform(self, asset):
        """ overload function from parent"""
        # do something specific
        return asset
