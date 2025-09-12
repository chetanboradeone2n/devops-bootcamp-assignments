import unittest
import requests

class TestStudentsAPI(unittest.TestCase):

    def test_healthcheck(self):
        response = requests.get('http://localhost:8080/api/v1/healthcheck', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['status'], 'ok')
    
    def test_get_all_students(self):
        response = requests.get('http://localhost:8080/api/v1/students', timeout=5)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_create_and_get_student(self):
        student_data = {"name": "test1", "email": "test1@example.com", "age": 20}
        create_response = requests.post('http://localhost:8080/api/v1/students', json=student_data, timeout=5)
        self.assertEqual(create_response.status_code, 201)
        student_id = create_response.json()['id']    
        get_response = requests.get(f'http://localhost:8080/api/v1/students/{student_id}', timeout=5)
        self.assertEqual(get_response.status_code, 200)
        self.assertIsInstance(get_response.json(), dict)

if __name__ == '__main__':
    unittest.main()