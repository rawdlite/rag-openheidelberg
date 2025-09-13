import unittest


class TestCouncilInsights(unittest.TestCase):
    
    def setUp(self):
        from collecting.councilinsights import CouncilInsights
        # Initialize client with real config
        self.insights = CouncilInsights()

    def test_init(self):
        # Initialize CouncilInsights with real config
        self.assertIsInstance(self.insights.start_id, int)
        self.assertIsInstance(self.insights.end_id, int)  
        self.assertIsInstance(self.insights.base_url, str)
        
    def test_process(self):
        self.insights.process()
        self.assertTrue(True) 
        
class TestLocalFiles(unittest.TestCase):
    
    def setUp(self):
        from collecting.localfiles import FileScanner
        # Initialize client with real config
        self.file_scanner = FileScanner()

    def test_init(self):
        # Initialize CounsilInsights with real config
        self.assertIsInstance(self.file_scanner.path, str)
        self.assertIsInstance(self.file_scanner.format, str)
        
    def test_process(self):
        self.file_scanner.process()
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()