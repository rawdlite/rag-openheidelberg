import boto3
import os
import io
from config import Config

class S3Client:
    """Basic S3 Client"""
    
    def __init__(self) -> None:
        self.config = Config().get('s3')
        self.s3 = boto3.resource(
            's3',
            aws_access_key_id=self.config['aws_access_key_id'] ,
            aws_secret_access_key=self.config['aws_secret_access_key'],
            region_name=self.config['region_name'] ,
            endpoint_url=self.config['endpoint_url']
        )
        self.db = self.s3.Bucket(self.config['bucket_name'])
        
    def save_local_file(self, file_path: str):
        file_name =  os.path.basename(file_path)
        self.db.upload_file(file_path, file_name)
        
    def save_stream(self, data, key):
        self.db.upload_fileobj(io.BytesIO(data), key)
        
    def get_asset(self, key: str):
        self.client.get_object(
            Bucket=self.config['bucket_name'],
            Key=key
        )
    
    def get_fileobj(self, key: str):
        data = self.db.download_fileobj(key)
        return data