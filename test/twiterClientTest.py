import unittest

class TestClientMethods(unittest.TestCase):

    def test_get_user_params_from_twitter(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()