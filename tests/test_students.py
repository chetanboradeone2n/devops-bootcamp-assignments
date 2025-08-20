import unittest
import requests

class TestStudentsAPI(unittest.TestCase):

    def test_healthcheck(self):
#       print("Testing the healthcheck endpoint")
        response = requests.get('http://localhost:5000/api/v1/healthcheck')
#       print(f"Response: {response.status_code}, {response.text}")
#       print(f" Response JSON: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'],'ok')
    
    def test_get_all_students(self):
#       print("testing the get all students endpoint")
        response = requests.get('http://localhost:5000/api/v1/students')
#       print(f"Response: {response.status_code}, {response.text}")
#       print(f" Response JSON: {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

if __name__ == '__main__':
    unittest.main()

