from couchdbclient import Client
from config import Config
from s3client import S3Client

class Categorizer:
    """Base Class for categorizing Pdf Files"""

    def __init__(self):
        self.config = Config().get('categorizer')
        self.client = Client()
        self.s3_client = S3Client()
        self.s3_resource = self.s3_client.s3
        self.s3_bucket = self.s3_client.db
        
    def get_assets(self) -> list:
        assets = self.client.get_all_pdfs()
        return [asset.doc for asset in assets]
    
    def save_asset(self, asset):
        self.client.db.put(asset)