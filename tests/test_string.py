import unittest

import upils.string as upils_string


class StringTest(unittest.TestCase):
    def test_camel_case_to_snake_case(self):
        camel_string = "CamelCase"
        snake_string = upils_string.camel_case_to_snake_case(camel_string)
        self.assertEqual("camel_case", snake_string)


if __name__ == "__main__":
    unittest.main()
