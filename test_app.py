import unittest
import requests

BASE_URL = "http://localhost:8080"

class FlaskLocalApiTestCase(unittest.TestCase):

    def test_home(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello", response.json()["message"])

    def test_about(self):
        response = requests.get(f"{BASE_URL}/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn("sample Flask API", response.json()["about"])

    def test_echo_valid(self):
        payload = {"name": "Ezekiel"}
        response = requests.post(f"{BASE_URL}/echo", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), {"you_sent": payload})

    def test_add_valid(self):
        payload = {"a": 5, "b": 3}
        response = requests.post(f"{BASE_URL}/add", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 8.0})

    def test_add_missing_param(self):
        payload = {"a": 5}
        response = requests.post(f"{BASE_URL}/add", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing a or b", response.json()["error"])

    def test_add_invalid_type(self):
        payload = {"a": "five", "b": 2}
        response = requests.post(f"{BASE_URL}/add", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("a and b must be numbers", response.json()["error"])


if __name__ == "__main__":
    unittest.main()