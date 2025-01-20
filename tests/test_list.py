import unittest

from upils import list as upils_list


class ListCase(unittest.TestCase):
    def test_string_list(self):
        list_input = ["1", "1", "2", "2", "3"]
        expected = ["1", "2", "3"]
        res = upils_list.get_unique_list(list_input)
        self.assertCountEqual(res, expected)

    def test_num_list(self):
        list_input = [1, 2, 2, 2, 3, 3]
        expected = [1, 2, 3]
        res = upils_list.get_unique_list(list_input)
        self.assertCountEqual(res, expected)


if __name__ == "__main__":
    unittest.main()
