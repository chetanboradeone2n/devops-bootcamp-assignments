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

    def test_create_and_get_student(self):
        student_data = {"name": "test1", "email": "test1@example.com", "age": 20}
        create_response = requests.post('http://localhost:5000/api/v1/students', json=student_data)
        self.assertEqual(create_response.status_code, 201)  # Assuming 201 for creation    
        student_id = create_response.json()['id']    
        get_response = requests.get(f'http://localhost:5000/api/v1/students/{student_id}')
        self.assertEqual(get_response.status_code, 200)
        self.assertIsInstance(get_response.json(), dict)


if __name__ == '__main__':
    unittest.main()

