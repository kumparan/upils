import unittest
from datetime import datetime
from upils import datetime


class DTCase(unittest.TestCase):
    def test_rfc3339(self):
        d: datetime = datetime(2009, 10, 5, 18, 00)
        rfc: str = datetime.to_rfc3339(d)
        self.assertEqual(rfc, "2009-10-05T18:00:00.000000Z")  # add assertion here


if __name__ == '__main__':
    unittest.main()
