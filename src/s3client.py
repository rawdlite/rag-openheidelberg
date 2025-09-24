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
        self.db.upload_fileobj(io.BytesIO(data.encode()), key)
        
    def get_asset(self, key: str):
        self.client.get_object(
            Bucket=self.config['bucket_name'],
            Key=key
        )
    
    def get_fileobj(self, key: str):
        data = self.db.download_fileobj(key)
        return data
    
    def get_pdf(self, asset: dict) -> dict:
        pdf_path = asset.get('storage', {}).get('pdf').get('path')
        if not pdf_path:
            return {'status': 'error',
                    'msg': "pdf_path not found"
            }
        pdf_path_parts = pdf_path.split('/')
        if pdf_path_parts[0] != 's3:':
            return {'status': 'error',
                    'msg': "S3 supported by this method"
                    }
        key = pdf_path_parts[-1]
        bucket_name = pdf_path_parts[-2]
        pdf_content = io.BytesIO()
        # Use bucket name in case path is referencing a bucket other than configurerd one
        self.s3.Bucket(bucket_name).download_fileobj(Key=key,Fileobj=pdf_content)
        return {'status': 'ok',
                'pdf_content': pdf_content
        }