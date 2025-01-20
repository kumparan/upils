import unittest
from datetime import datetime, timedelta, timezone

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

    def test_to_timestamp_millis_from_str_tz(self):
        dt_utc7: str
        dt_utc7 = "2023-01-01T08:00:00+07:00"
        dt_millis = upils_datetime.to_timestamp_millis(dt_utc7)
        dt_utc = datetime.utcfromtimestamp(dt_millis / 1000)
        self.assertEqual(dt_utc.day, 1)
        self.assertEqual(dt_utc.hour, 8)  # not timezone_aware
        self.assertEqual(dt_utc.minute, 0)
        self.assertEqual(dt_utc.second, 0)

    def test_to_timestamp_millis_from_datetime(self):
        dt: str
        dt = datetime(year=2023, month=1, day=1, hour=1, minute=0, second=15)
        dt_millis = upils_datetime.to_timestamp_millis(dt)
        dt_utc = datetime.utcfromtimestamp(dt_millis / 1000)
        self.assertEqual(dt_utc.day, 1)
        self.assertEqual(dt_utc.hour, 1)
        self.assertEqual(dt_utc.minute, 0)
        self.assertEqual(dt_utc.second, 15)

    def test_to_timestamp_without_timezone_literal(self):
        dt = datetime(2023, 1, 1, 7, 0, 0)
        dt = upils_datetime.to_timestamp_without_timezone_literal(dt)
        self.assertEqual(dt, "2023-01-01 07:00:00")

        dt = datetime(2023, 1, 1, 7, 1, 50, 999)
        dt = upils_datetime.to_timestamp_without_timezone_literal(dt)
        self.assertEqual(dt, "2023-01-01 07:01:50")

        dt = datetime(2023, 1, 1, 12, 15, 30, 999, tzinfo=pytz.UTC)
        dt = upils_datetime.to_timestamp_without_timezone_literal(dt)
        self.assertEqual(dt, "2023-01-01 12:15:30")

    def test_to_datetime_with_timezone(self):
        datetime_literal = "2024-04-01"
        datetime_format = "%Y-%m-%d"
        dt_expected = datetime(2024, 4, 1, 0, 0, 0, 000, tzinfo=pytz.UTC)
        dt_actual = upils_datetime.to_datetime_with_timezone(
            datetime_literal, datetime_format
        )
        self.assertEqual(dt_expected, dt_actual)

        datetime_literal = "2024-04-01 07:00:00"
        datetime_format = "%Y-%m-%d %H:%M:%S"
        dt_expected = datetime(2024, 4, 1, 7, 0, 0, 000, tzinfo=pytz.UTC)
        dt_actual = upils_datetime.to_datetime_with_timezone(
            datetime_literal, datetime_format
        )
        self.assertEqual(dt_expected, dt_actual)

        datetime_literal = "2024-04-01 07:00:00+0000"
        datetime_format = "%Y-%m-%d %H:%M:%S%z"
        dt_expected = datetime(2024, 4, 1, 7, 0, 0, 000, tzinfo=pytz.UTC)
        dt_actual = upils_datetime.to_datetime_with_timezone(
            datetime_literal, datetime_format
        )
        self.assertEqual(dt_expected, dt_actual)

        datetime_literal = "2024-04-01 07:00:00+0700"
        datetime_format = "%Y-%m-%d %H:%M:%S%z"
        dt_expected = datetime(
            2024, 4, 1, 7, 0, 0, 000, tzinfo=timezone(timedelta(hours=7))
        )
        dt_actual = upils_datetime.to_datetime_with_timezone(
            datetime_literal, datetime_format
        )
        self.assertEqual(dt_expected, dt_actual)

        datetime_literal = "2024-04-01 07:00:00-1200"
        datetime_format = "%Y-%m-%d %H:%M:%S%z"
        dt_expected = datetime(
            2024, 4, 1, 7, 0, 0, 000, tzinfo=timezone(timedelta(days=-1, hours=12))
        )
        dt_actual = upils_datetime.to_datetime_with_timezone(
            datetime_literal, datetime_format
        )
        self.assertEqual(dt_expected, dt_actual)


if __name__ == "__main__":
    unittest.main()
