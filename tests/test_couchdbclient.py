import unittest
from couchdbclient import Client

class TestCouchDBClient(unittest.TestCase):
    def setUp(self):
        # Initialize client with real config
        self.client = Client()
        
        
    def test_get_all_docs(self):
        # Act
        result = self.client.get_all_docs()
        # Assert
        self.assertIsInstance(result, list)
        
    def test_get_unrun_doc_page(self):
        limit = 5
        skip = 3
        result = self.client.get_all_unrun_docs(limit=limit,skip=skip)
        self.assertEqual(len(result),limit)
        
    def test_get_unconverted_doc(self):
        limit = 10
        skip = 5
        result = self.client.get_all_unconverted_docs(limit=limit,skip=skip)
        self.assertEqual(len(result),limit)

if __name__ == "__main__":
    unittest.main()