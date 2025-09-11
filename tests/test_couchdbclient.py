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


if __name__ == "__main__":
    unittest.main()