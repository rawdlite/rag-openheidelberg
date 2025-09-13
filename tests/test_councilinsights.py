import unittest
from collecting.councilinsights import CounsilInsights

class TestCounsilInsights(unittest.TestCase):

    def test_init(self):
        # Initialize CounsilInsights with real config
        insights = CounsilInsights()
        self.assertIsInstance(insights.start_id, int)
        self.assertIsInstance(insights.end_id, int)  
        self.assertIsInstance(insights.base_url, str)
        
    def test_process(self):
        insights = CounsilInsights()
        insights.process()
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()
