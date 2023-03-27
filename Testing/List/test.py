import unittest

from extended_list import IntegerList


class List(unittest.TestCase):

    def setUp(self) -> None:
        self.integer_list = IntegerList(1, 3, 2)

    def test_add_returns_list(self):
        self.integer_list.add(5)

        self.assertEqual(self.integer_list.get_data(), [1, 3, 2, 5])

    def test_add_raises_error_if_given_non_integere(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.add('a')

        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_remove_index_removes_an_element_and_returns_it(self):
        el = self.integer_list.remove_index(0)

        self.assertEqual(el, 1)

    def test_remove_index_raises_an_error_if_index_equals_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(3)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_remove_index_raises_an_error_if_index_is_greater_than_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(5)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_instance_takes_only_integers(self):
        [self.failIf(type(el) != int) for el in self.integer_list.get_data()]

    def test_get_returns_smt(self):
        el = self.integer_list.get(0)

        self.assertEqual(el, 1)

    def test_get_returns_error_if_index_is_equal_to_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(3)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_get_returns_error_if_index_is_greater_than_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(10)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_inserts_stuff(self):
        self.integer_list.insert(1, 5)

        self.assertEqual(self.integer_list.get_data(), [1, 5, 3, 2])

    def test_insert_returns_error_if_index_is_equal_to_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(3, 5)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_returns_error_if_index_is_greater_than_len(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(5, 5)

        self.assertEqual(str(context.exception), "Index is out of range")

    def test_insert_returns_error_if_invalid_value_is_given(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(1, 'a')

        self.assertEqual(str(context.exception), "Element is not Integer")

    def test_get_biggest(self):
        el = self.integer_list.get_biggest()

        self.assertEqual(el, 3)

    def test_get_index(self):
        el = self.integer_list.get_index(3)

        self.assertEqual(el, 1)


if __name__ == "__main__":
    unittest.main()