import requests
import datetime
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from s3client import S3Client
from couchdbclient import Client

class Retriever:
    """Get list of Assets from couchdb,
    retrieve them and store in S3 Bucket.
    """
    
    def __init__(self) -> None:
        self.client = Client()
        self.s3 = S3Client()
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=0.5,
            status_forcelist=[500, 502, 503, 504],
            allowed_methods=["HEAD", "GET"]
        )
        adapter = HTTPAdapter(max_retries=retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
        self.session.headers.update({
            "User-Agent": "RAG-Openheidelberg/1.0"
        })
        
    def process(self):
        assets = self.get_assets()
        for asset in assets:
            doc = self.transform(asset.doc)
            self.save_asset(doc)
            
    def get_assets(self) -> list:
        assets = self.client.get_all_unrun_docs()
        return assets
    
    def request_url(self, url: str) -> dict:
        try:
            head_resp = self.session.head(url, timeout=5)
        except requests.RequestException as e:
            return {'status': e}
        content_type = head_resp.headers.get('Content-Type', '')
        result = {'status': head_resp.status_code,
                  'content_type': content_type}
        if head_resp.status_code != 200:
            return result
        if not content_type.startswith('application/pdf'):
            return result
        try:
            response = self.session.get(url, stream=True, timeout=10)
        except requests.RequestException as e:
            result['status': e]
            return result
        result['status'] = response.status_code
        if response.status_code == 200:
            result['content'] = response.content
        return result

            
    def transform(self, asset: dict) -> dict:
        url = asset.get('retrieval', {}).get('url')
        key = f"{asset.get('id')}.pdf"
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        storage = False
        if url and url.startswith('file'):
            file_name = url.replace("file://", "")
            self.s3.save_local_file(file_name)
            asset['retrieval']['last_run'] = now
            storage = True
        elif url.startswith('http'):
            result = self.request_url(url)
            if result.get('content_type'):
                asset['retrieval']['content_type'] = result['content_type']
            asset['retrieval']['status'] = result['status']
            asset['retrieval']['last_run'] = now
            if result.get('content'):
                data = result['content']
                self.s3.save_stream(data=data,key=key)
                storage = True
        #TODO: add rclone
        if storage:
            asset['storage'] = {
                'pdf': {
                    'path': f"s3://{self.s3.db._name}/{key}",
                    'created_at': now
                }
            }
        return asset
        
    def save_asset(self, asset):
        self.client.db.put(asset)

def main():
    retriever = Retriever()
    retriever.process()
    
if __name__ == '__main__':
    main()