import unittest
import requests
import httpretty
from methods import Token, Restricted



class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.validate = Restricted()


    def test_hc01(self):
        response = requests.get('http://service.local:8000/')
        self.assertEqual(response.status_code, 200)

    @httpretty.activate
    def test_hc02(self):
        httpretty.register_uri(httpretty.GET, "http://service.local:8000/_health", body="OK")
        # use!
        response = requests.get('http://service.local:8000/_health')
        self.assertEqual(response.text, 'OK')

    def test_generate_token(self):
        self.assertEqual('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI', self.convert.generate_token('admin', 'secret'))

    def test_access_data(self):
        self.assertEqual('You are under protected data', self.validate.access_data('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoiYWRtaW4ifQ.StuYX978pQGnCeeaj2E1yBYwQvZIodyDTCJWXdsxBGI'))

if __name__ == '__main__':
    unittest.main()
