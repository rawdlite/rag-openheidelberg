import unittest

class TestDoclingConverter(unittest.TestCase):
    
    def setUp(self):
        from converting.docling_converter import DoclingConverter
        # Initialize client with real config
        self.converter = DoclingConverter()

        
    def test_process(self):
        self.converter.process()
        self.assertTrue(True) 