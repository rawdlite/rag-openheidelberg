import unittest
from s3client import S3Client

class TestS3Client(unittest.TestCase):
    
    def setUp(self):
        # Initialize client with real config
        self.s3client = S3Client()
        
    def test_save_asset(self):
        file_path = "/Users/tom/Gebratener Spinat.pdf"
        self.s3client.save_asset(file_path)
        self.assertTrue(True)
        