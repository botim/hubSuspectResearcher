import unittest

class TestVisualizationMethods(unittest.TestCase):
	
	#consume features csv
    def test_load_features(self):
        self.assertEqual('foo'.upper(), 'FOO')

	#visualize features
    def test_feature_visualization(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

if __name__ == '__main__':
    unittest.main()