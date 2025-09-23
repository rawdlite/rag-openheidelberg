import unittest
from collecting.councilinsights import CouncilInsights

class TestCounsilInsights(unittest.TestCase):

    def test_init(self):
        # Initialize CounsilInsights with real config
        insights = CouncilInsights()
        self.assertIsInstance(insights.start_id, int)
        self.assertIsInstance(insights.end_id, int)  
        self.assertIsInstance(insights.base_url, str)
        
    def test_process(self):
        insights = CouncilInsights()
        insights.process()
        self.assertTrue(True) 

if __name__ == '__main__':
    unittest.main()
