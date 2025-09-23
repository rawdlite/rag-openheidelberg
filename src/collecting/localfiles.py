import os
from collecting.collector import Collector

class FileScanner(Collector):
    """ Generates a AssetURIList from local files """
    
    def __init__(self):
        super().__init__()
        self.path = self.config.get('localfiles').get('path')
        self.format = self.config.get('localfiles').get('format')
        
    def process(self):
        assets = self.get_assets()
        for asset in assets:
            doc = self.transform(asset)
            self.save_asset(doc)
            
    def get_assets(self) -> list:
        files = []
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file() and entry.name.endswith(self.format):
                    files.append(entry)
        return files 
    
    def transform(self, asset: dict) -> dict:
        doc = {
            'id': os.path.splitext(asset.name)[0],
            'retrieval': {
                'url': f"file://{asset.path}",
                'last_run': None,
                'status': 200
                }
	        }
        return doc
    
def main():
    file_scanner = FileScanner()
    file_scanner.process()
    
if __name__ == '__main__':
    main()
        