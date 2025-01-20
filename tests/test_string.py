import hashlib
import unittest

from upils import string as upils_string


class StringCase(unittest.TestCase):
    def test_hash_and_encode_to_base64(self):
        expected_base64_string = "gStIZtdCBFym9YM884kKewVZE3Vw8voFmVe1tMr2pRo="
        string_data = "test_string_to_hash"
        actual_base64_string = upils_string.hash_and_encode_to_base64(
            data=string_data, hash_function=hashlib.sha256
        )
        self.assertEqual(expected_base64_string, actual_base64_string)


if __name__ == "__main__":
    unittest.main()
