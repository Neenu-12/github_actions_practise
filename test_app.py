import unittest
from app import app

class BasicTests(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_root(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Hello, CI/CD', res.data)

if __name__ == "__main__":
    unittest.main()
