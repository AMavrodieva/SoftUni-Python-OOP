from project_unitest.library import Library

from unittest import TestCase, main


class TestLibrary(TestCase):
    NAME = "NL"

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.library.name)
        self.assertDictEqual({}, self.library.books_by_authors)
        self.assertDictEqual({}, self.library.readers)

    def test__set_name_when_not_value__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.library.name = ""
        self.assertEqual("Name cannot be empty string!", str(context.exception))

    def test__add_book__when_author_or_title_are_not_exist__expected_to_add_them(self):
        author_1, author_2 = "Mariya", "Georgi"
        tittle_1, tittle_2 = 'test1', 'test2'
        self.library.add_book(author_1, tittle_1)
        self.library.add_book(author_1, tittle_2)
        self.library.add_book(author_2, tittle_2)
        self.assertEqual(2, len(self.library.books_by_authors))
        self.assertIn(tittle_2, self.library.books_by_authors[author_1])
        expected_dict = {author_1: [tittle_1, tittle_2], author_2: [tittle_2]}
        self.assertDictEqual(expected_dict, self.library.books_by_authors)

    def test__add_reader__when_reader_exist__expected_return_str(self):
        name = "Reader1"
        self.library.add_reader(name)
        self.assertIn(name, self.library.readers)
        self.assertListEqual([], self.library.readers[name])
        result = self.library.add_reader(name)
        self.assertEqual(f"{name} is already registered in the {self.NAME} library.", result)

    def test__rent_book__when_reader_name_not_in_register__expected_correct_str(self):
        name, b_author, title = "Reader1", "Author1", "test1"
        result = self.library.rent_book(name, b_author, title)
        self.assertEqual(f"{name} is not registered in the {self.NAME} Library.", result)

    def test__rent_book__when_author_name_not_in_register__expected_correct_str(self):
        name, b_author, title = "Reader1", "Author1", "test1"
        self.library.readers[name] = []
        result = self.library.rent_book(name, b_author, title)
        self.assertEqual(f"{self.NAME} Library does not have any {b_author}'s books.", result)

    def test__rent_book__when_title_not_in_register__expected_correct_str(self):
        name, b_author, title = "Reader1", "Author1", "test1"
        self.library.readers[name] = []
        self.library.books_by_authors[b_author] = []
        result = self.library.rent_book(name, b_author, title)
        self.assertEqual(f"""{self.NAME} Library does not have {b_author}'s "{title}".""", result)

    def test__rent_book__when_all_value_are_valid__expected_add_book_in_reader_list_and_del_in_library(self):
        name, b_author, title = "Reader1", "Author1", "test1"
        self.library.readers[name] = []
        self.library.books_by_authors[b_author] = [title]
        self.library.rent_book(name, b_author, title)
        self.assertEqual({name: [{b_author: title}]}, self.library.readers)
        self.assertListEqual([], self.library.books_by_authors[b_author])


if __name__ == "__main__":
    main()

