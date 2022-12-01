from project_tasks.cat import Cat
"""
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping

"""
from unittest import TestCase, main


class CatTests(TestCase):
    NAME = 'Tom'

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test__init__when_valid_props_expected_correct_value(self):
        self.assertEqual(self.NAME, self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test__eat__when_cat_fed__expected_to_raise_error(self):
        self.cat.eat()
        with self.assertRaises(Exception) as error:
            self.cat.eat()
        self.assertEqual('Already fed.', str(error.exception))

    def test__eat__when_cat_eat__expected_fed_and_sleep_to_be_true(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test__eat__when_cat_eat__expected_size_to_incremented(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)

    def test__sleep__when_cat_not_fed__expected_to_raise_exception(self):
        with self.assertRaises(Exception) as error:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(error.exception))

    def test__sleep__when_cat_fed__expected_correct_result(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    main()
