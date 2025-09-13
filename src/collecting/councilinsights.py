from collecting.collector import Collector
from config import Config

class CouncilInsights(Collector):

    def __init__(self):
        super().__init__()
        config = Config().get('collector').get('council-insights')
        self.start_id = config.get('start_id')
        self.end_id = config.get('end_id')
        self.base_url = config.get('base_url')
        


    def process(self):
        #TODO: get highest ID from DB and set start_id
        for id in range(self.start_id, self.end_id):
            url = f"{self.base_url}?id={id}&type=do"
            asset = {
                'id': id,
                'retrieval': {
                    'url': url,
                    'last_run': None,
                    'status': None
                    }
	        }
            self.save_asset(asset)

def main():
    insights = CouncilInsights()
    insights.process()
    
if __name__ == '__main__':
    main()