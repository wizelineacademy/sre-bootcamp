import unittest
from methods import Token, Restricted


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()

    def test_generate_token(self):
        self.assertEqual('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9.S-NySRxO4tEJyPGmK_sqJD52loTkUxbxX1Lp0yq5Cco', self.convert.generate_token('admin'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9.S-NySRxO4tEJyPGmK_sqJD52loTkUxbxX1Lp0yq5Cco'))

if __name__ == '__main__':
    unittest.main()
