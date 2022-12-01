from all_exercise.project.mammal import Mammal
# from project.all_exercise import Mammal

from unittest import TestCase, main


class TestMammal(TestCase):
    NAME = "TigerCat"
    MAMMAL_TYPE = 'tiger'
    SOUND = 'Brr'
    KINGDOM = 'animals'

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test__make_sound__expected_corrected_string(self):
        actual_result = self.mammal.make_sound()
        expected_result = f"{self.NAME} makes {self.SOUND}"
        self.assertEqual(expected_result, actual_result)

    def test__get_kingdom__expected_correct_result(self):
        actual_result = self.mammal.get_kingdom()
        expected_result = self.KINGDOM
        self.assertEqual(expected_result, actual_result)

    def test__info__expected_correct_result(self):
        actual_result = self.mammal.info()
        expected_result = f"{self.NAME} is of type {self.MAMMAL_TYPE}"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
