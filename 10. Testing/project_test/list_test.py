from project_tasks.extended_list import IntegerList


from unittest import TestCase, main


class ListTests(TestCase):
    ARGUMENTS = [1, 2, 3, 4]

    def setUp(self) -> None:
        self.list = IntegerList(self.ARGUMENTS)

    def test__initialized_correctly_with_without_data(self):
        list_1 = IntegerList([])
        result = list_1._IntegerList__data
        self.assertEqual([], result)

    def test__initialized_correctly_with_with_wrong_data(self):
        list_1 = IntegerList(['wrong', 10.5])
        result = list_1._IntegerList__data
        self.assertEqual([], result)

    def test__initialized_correctly_with_with_integer_data(self):
        list_1 = IntegerList(*self.ARGUMENTS, 'wrong')
        result = list_1._IntegerList__data
        self.assertEqual(self.ARGUMENTS, result)

    def test_get_data__expected_to_return_correct_result(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        result = list_1.get_data()
        self.assertEqual(self.ARGUMENTS, result)

    def test__add__when_element_is_not_integer__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as error:
            self.list.add("asd")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test__add__when_element_is_integer__expected_list_to_incremented(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        list_1.add(5)
        self.assertEqual(len(self.ARGUMENTS)+1, len(list_1._IntegerList__data))

    def test__remove_index__when_index_is_out_of_range__expected_to_raise_exception(self):
        with self.assertRaises(IndexError) as error:
            self.list.remove_index(4)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__remove_index__when_index_is_valid__expected_to_return_correct_result(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        result = list_1.remove_index(3)
        self.assertEqual(4, result)

    def test__get__when_index_is_out_of_range__expected_to_raise_exception(self):
        with self.assertRaises(IndexError) as error:
            self.list.get(4)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__get__when_index_is_valid__expected_correctly_value(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        result = list_1.get(3)
        self.assertEqual(4, result)

    def test__insert__when_index_is_out_of_range__expected_to_raise_exception(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        with self.assertRaises(IndexError) as error:
            list_1.insert(4, 5)
        self.assertEqual("Index is out of range", str(error.exception))

    def test__insert__when_element_is_not_integer__expected_to_raise_exception(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        with self.assertRaises(ValueError) as error:
            list_1.insert(2, "asd")
        self.assertEqual("Element is not Integer", str(error.exception))

    def test__insert__when_index_and_element_are_valid__expected_list_to_incremented(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        list_1.insert(2, 5)
        self.assertEqual(len(self.ARGUMENTS)+1, len(list_1._IntegerList__data))

    def test__get_biggest__expected_return_correct_result(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        result = list_1.get_biggest()
        self.assertEqual(4, result)

    def test__get_index__expected_return_correct_result(self):
        list_1 = IntegerList(*self.ARGUMENTS)
        result = list_1.get_index(2)
        self.assertEqual(1, result)


if __name__ == "__main__":
    main()