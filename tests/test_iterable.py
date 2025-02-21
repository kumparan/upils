from upils.iterable import replace_none_in_iterable
import unittest


class IterableCase(unittest.TestCase):
    def test_replace_empty_value_in_list_returns_no_none(self):
        list_with_none = [None, "u", "i", "i", "a", "i"]
        replacement = ""
        list_no_none = replace_none_in_iterable(list_with_none, replacement)
        self.assertTrue(None not in list_no_none)

    def test_replace_empty_value_in_tuple_with_none_raises_error(self):
        tuple_with_none = (None, "u", "i", "i", "a", "i")
        replacement = None
        with self.assertRaises(ValueError):
            replace_none_in_iterable(tuple_with_none, replacement)

if __name__ == "__main__":
    unittest.main()
