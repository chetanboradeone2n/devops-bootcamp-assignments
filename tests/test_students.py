import unittest
import requests

class TestStudentsAPI(unittest.TestCase):

    def test_healthcheck(self):
        response = requests.get('http://localhost:5000/api/v1/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {status: 'ok'})

if __name__ == '__main__':
    unittest.main()

    