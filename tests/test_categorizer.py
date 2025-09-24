import unittest

class TestPdfParser(unittest.TestCase):
    
    def setUp(self):
        from categorizing.pdfparser import PDFParser
        # Initialize client with real config
        self.parser = PDFParser()

    def test_process(self):
        self.parser.process()
        self.assertTrue(True)