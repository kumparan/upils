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

    def test_datetime_to_timestamp_millis_from_str_tz(self):
        dt_utc7: str
        dt_utc7 = "2023-01-01T08:00:00+07:00"
        dt_millis = upils_datetime.datetime_to_timestamp_millis(dt_utc7)
        dt_utc = datetime.utcfromtimestamp(dt_millis / 1000)
        self.assertEqual(dt_utc.day, 1)
        self.assertEqual(dt_utc.hour, 8) # not timezone_aware
        self.assertEqual(dt_utc.minute, 0)
        self.assertEqual(dt_utc.second, 0)
        
    def test_datetime_to_timestamp_millis_from_datetime(self):
        dt: str
        dt = datetime(year=2023, month=1, day=1, hour=1, minute=0, second=15)
        dt_millis = upils_datetime.datetime_to_timestamp_millis(dt)
        dt_utc = datetime.utcfromtimestamp(dt_millis / 1000)
        self.assertEqual(dt_utc.day, 1)
        self.assertEqual(dt_utc.hour, 1)
        self.assertEqual(dt_utc.minute, 0)
        self.assertEqual(dt_utc.second, 15)


if __name__ == "__main__":
    unittest.main()
