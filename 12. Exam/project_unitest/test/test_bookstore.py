# from project_unitest.bookstore import Bookstore
from project_unitest.bookstore import Bookstore
from unittest import TestCase, main


class TestBookstore(TestCase):
    BOOK_LIMIT = 10

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOK_LIMIT)

    def test__initialized_correctly(self):
        self.assertEqual(self.BOOK_LIMIT, self.bookstore.books_limit)
        self.assertDictEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test__total_sold_books__expected_to_return_correct_result(self):
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test__total_sold_books__when_is_available_books__expected_to_return_correct_result(self):
        self.bookstore._Bookstore__total_sold_books = 1
        self.assertEqual(1, self.bookstore.total_sold_books)

    def test__books_limit__when_value_is_negative__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            value = -1
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(context.exception))
        self.assertIsNotNone(str(context.exception))

    def test__books_limit__when_value_is_zero__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            value = 0
            self.bookstore.books_limit = value
        self.assertEqual(f"Books limit of {value} is not valid", str(context.exception))
        self.assertIsNotNone(str(context.exception))

    def test__books_limit__when_value_is_valid__expected_to_return_correct_result(self):
        value = 1
        self.bookstore.books_limit = value
        self.assertEqual(value, self.bookstore.books_limit)

    def test__len__when_count_is_empty_expected_to_return_zero(self):
        self.assertEqual(0, self.bookstore.__len__())

    def test__len__when_is_available_books_expected_to_return_correct_result(self):
        book_1, book_2 = "Book_1", "Book_2"
        self.bookstore.availability_in_store_by_book_titles[book_1] = 1
        self.bookstore.availability_in_store_by_book_titles[book_2] = 2
        self.assertEqual(3, self.bookstore.__len__())
        self.assertDictEqual({book_1: 1, book_2: 2}, self.bookstore.availability_in_store_by_book_titles)

    def test__receive_book__when_not_enough_space_in_bookstore_expected_to_raise_exception(self):
        self.bookstore.books_limit = 2
        book_1, book_2 = "Book_1", "Book_2"
        self.bookstore.availability_in_store_by_book_titles[book_1] = 1
        with self.assertRaises(Exception) as context:
            self.bookstore.receive_book(book_2, 2)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(context.exception))
        self.assertIsNotNone(str(context.exception))
        self.assertDictEqual({book_1: 1}, self.bookstore.availability_in_store_by_book_titles)


    def test__receive_book__when_book_with_available_books_equal_limit__expected_to_add_and_correct_str(self):
        self.bookstore.books_limit = 2
        book_1, count = "Book_1", 1
        book_2, count_2 = "Book_2", 1
        self.bookstore.availability_in_store_by_book_titles[book_1] = 1
        result = self.bookstore.receive_book(book_2, count_2)
        self.assertIn(book_2, self.bookstore.availability_in_store_by_book_titles)
        expected_result = f"{count} copies of {book_2} are available in the bookstore."
        self.assertEqual(expected_result, result)
        self.assertDictEqual({book_1: 1, book_2: 1}, self.bookstore.availability_in_store_by_book_titles)

    def test__receive_book__when_is_enough_and_book_name_not_in_store__expected_to_add_and_correct_str(self):
        book_1, count = "Book_1", 1
        result = self.bookstore.receive_book(book_1, count)
        self.assertIn(book_1, self.bookstore.availability_in_store_by_book_titles)
        expected_result = f"{count} copies of {book_1} are available in the bookstore."
        self.assertEqual(expected_result, result)

    def test__receive_book__when_is_enough_and_book_name_is_in_store__expected_to_add_and_correct_str(self):
        self.bookstore.books_limit = 4
        book_1, count = "Book_1", 1
        self.bookstore.availability_in_store_by_book_titles[book_1] = 1
        result = self.bookstore.receive_book(book_1, count)
        self.assertIn(book_1, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(2, self.bookstore.availability_in_store_by_book_titles[book_1])
        expected_result = f"{2} copies of {book_1} are available in the bookstore."
        self.assertEqual(expected_result, result)

    def test__sell_book__when_book_not_exist__expected_to_raise_exception(self):
        book_1, count = "Book_1", 1
        with self.assertRaises(Exception) as context:
            self.bookstore.sell_book(book_1, count)
        self.assertNotIn(book_1, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"Book {book_1} doesn't exist!", str(context.exception))
        self.assertIsNotNone(str(context.exception))

    def test__sell_book__when_books_count_is_not_enough__expected_to_raise_exception(self):
        book_1, count = "Book_1", 1
        wanted_count = 2
        self.bookstore.availability_in_store_by_book_titles[book_1] = count
        with self.assertRaises(Exception) as context:
            self.bookstore.sell_book(book_1, wanted_count)
        self.assertEqual(f"{book_1} has not enough copies to sell. Left: {count}", str(context.exception))
        self.assertIsNotNone(str(context.exception))
        self.assertEqual(True, wanted_count > self.bookstore.availability_in_store_by_book_titles[book_1])

    def test__sell_book__when_value_are_valid__expected_books_in_store_to_decremented_and_return_correct_str(self):
        self.bookstore.books_limit = 4
        book_1, count = "Book_1", 2
        wanted_count = 1
        self.bookstore.availability_in_store_by_book_titles[book_1] = count
        result = self.bookstore.sell_book(book_1, wanted_count)
        expected_result = f"Sold {wanted_count} copies of {book_1}"
        self.assertEqual(expected_result, result)
        self.assertEqual(1, self.bookstore.__len__())
        self.assertEqual(1, self.bookstore.total_sold_books)
        self.assertEqual(False, wanted_count > self.bookstore.availability_in_store_by_book_titles[book_1])
        self.assertEqual(wanted_count, self.bookstore.total_sold_books)
        self.assertEqual(wanted_count, self.bookstore._Bookstore__total_sold_books)

    def test__str__expected_to_return_correct_result(self):
        book_1, count = "Book_1", 2
        book_2, count_2 = "Book_2", 1
        self.bookstore.availability_in_store_by_book_titles[book_1] = count
        self.bookstore.availability_in_store_by_book_titles[book_2] = count_2
        self.bookstore.sell_book(book_1, 1)
        expected_result = f"""Total sold books: 1
Current availability: {count}
 - {book_1}: 1 copies
 - {book_2}: 1 copies"""
        result = str(self.bookstore)
        self.assertEqual(expected_result, result)


if __name__ == "__main__":
    main()
