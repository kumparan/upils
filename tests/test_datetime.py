import unittest
from datetime import datetime

import pytz

from upils import datetime as upils_datetime


class DTCase(unittest.TestCase):
    def test_rfc3339(self):
        dt: datetime = datetime(2009, 10, 5, 18, 00)
        rfc_dt: str = upils_datetime.to_rfc3339(dt)
        self.assertEqual(rfc_dt, "2009-10-05T18:00:00.000000Z")  # add assertion here

    def test_utc7(self):
        dt = datetime(2009, 10, 5, 18, 0, 0, 0, tzinfo=pytz.UTC)
        utc7_dt = upils_datetime.to_utc7(dt)
        self.assertEqual(utc7_dt.day, 6)
        self.assertEqual(utc7_dt.hour, 1)
        self.assertEqual(utc7_dt.minute, 0)
        self.assertEqual(utc7_dt.second, 0)
        self.assertEqual(utc7_dt.microsecond, 0)
        self.assertIn(utc7_dt.tzname(), ["Asia/Jakarta", "WIB"])

        cst_tz = pytz.timezone("US/Central")
        dt = datetime(2009, 10, 5, 18, 0, 0, 0, tzinfo=cst_tz)
        utc7_dt = upils_datetime.to_utc7(dt)
        self.assertEqual(utc7_dt.day, 6)
        self.assertEqual(utc7_dt.hour, 6)
        self.assertEqual(utc7_dt.minute, 51)
        self.assertEqual(utc7_dt.second, 0)
        self.assertEqual(utc7_dt.microsecond, 0)
        self.assertIn(utc7_dt.tzname(), ["Asia/Jakarta", "WIB"])

        dt = datetime(2009, 10, 5, 18, 0, 0, 0)
        utc7_dt = upils_datetime.to_utc7(dt)
        self.assertEqual(utc7_dt.day, 6)
        self.assertEqual(utc7_dt.hour, 1)
        self.assertEqual(utc7_dt.minute, 0)
        self.assertEqual(utc7_dt.second, 0)
        self.assertEqual(utc7_dt.microsecond, 0)
        self.assertIn(utc7_dt.tzname(), ["Asia/Jakarta", "WIB"])

        dt = datetime(2009, 10, 5)
        utc7_dt = upils_datetime.to_utc7(dt)
        self.assertEqual(utc7_dt.day, 5)
        self.assertEqual(utc7_dt.hour, 7)
        self.assertEqual(utc7_dt.minute, 0)
        self.assertEqual(utc7_dt.second, 0)
        self.assertEqual(utc7_dt.microsecond, 0)
        self.assertIn(utc7_dt.tzname(), ["Asia/Jakarta", "WIB"])


if __name__ == "__main__":
    unittest.main()
