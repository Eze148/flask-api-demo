import unittest
import json
from app import app  # Assumes your Flask code is in `app.py`


class FlaskApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Hello, world!", response.get_data(as_text=True))

    def test_about(self):
        response = self.app.get("/about")
        self.assertEqual(response.status_code, 200)
        self.assertIn("sample Flask API", response.get_data(as_text=True))

    def test_echo_valid(self):
        payload = {"name": "Ezekiel"}
        response = self.app.post("/echo", json=payload)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.get_json(), {"you_sent": payload})

    def test_add_valid(self):
        payload = {"a": 5, "b": 3}
        response = self.app.post("/add", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"result": 8.0})

    def test_add_missing_param(self):
        payload = {"a": 5}
        response = self.app.post("/add", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing a or b", response.get_data(as_text=True))

    def test_add_invalid_type(self):
        payload = {"a": "five", "b": 2}
        response = self.app.post("/add", json=payload)
        self.assertEqual(response.status_code, 400)
        self.assertIn("a and b must be numbers", response.get_data(as_text=True))


if __name__ == "__main__":
    unittest.main()