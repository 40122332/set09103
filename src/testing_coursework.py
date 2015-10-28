import unittest
import coursework

class TestingTest(unittest.TestCase):
  def test_root(self):
    self.app=coursework.app.test_client()
    out=self.app.get('/')
    assert '200 OK' in out.status
    assert 'text/html' in out.content_type

if __name__ == "__main__":
  unittest.main()
