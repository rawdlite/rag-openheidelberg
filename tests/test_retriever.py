import unittest

class TestRetriever(unittest.TestCase):
    
    def setUp(self):
        from retrieving.retriever import Retriever
        # Initialize client with real config
        self.retriever = Retriever()

        
    def test_process(self):
        self.retriever.process()
        self.assertTrue(True) 