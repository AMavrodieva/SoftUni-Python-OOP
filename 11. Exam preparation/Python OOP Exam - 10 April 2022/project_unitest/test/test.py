from project_unitest.movie import Movie
# from project_unitest.movie import Movie

from unittest import TestCase, main


class TestMovie(TestCase):
    NAME = "Fast and Furious"
    YEAR = 2005
    RATING = 7

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertListEqual([], self.movie.actors)

    def test__set_name__expected_correct_result(self):
        movie_name = "test"
        self.movie.name = movie_name
        self.assertEqual(movie_name, self.movie.name)

    def test__set_name__when_name_is_empty_str__expected_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(context.exception))

    def test__set_year__expected_correct_result(self):
        movie_year = 1900
        self.movie.year = movie_year
        self.assertEqual(movie_year, self.movie.year)

    def test__set_year__when_year_is_less_than_1887__expected_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.movie.year = 1886
        self.assertEqual('Year is not valid!', str(context.exception))

    def test__add_actor__when_name_is_not_exist__expected_actors_to_incremented(self):
        current_actor = "Marian Keyes"
        self.movie.add_actor(current_actor)
        self.assertIn(current_actor, self.movie.actors)

    def test__add_actor__when_name_is_already_in_list__expected_to_return_correct_str(self):
        current_actor = "Marian Keyes"
        self.movie.add_actor(current_actor)
        result = self.movie.add_actor(current_actor)
        self.assertEqual(f"{current_actor} is already added in the list of actors!", result)

    def test__gt__when__rating_is_grater_than_other__expected_return_correct_str(self):
        movie_1 = Movie("Test", 2000, 3)
        first_result = str(self.movie > movie_1)
        expected_result = f'"{self.movie.name}" is better than "{movie_1.name}"'
        self.assertEqual(expected_result, first_result)

    def test__gt__when__other_rating_is_grater_than_current_rating__expected_return_correct_str(self):
        movie_2 = Movie("Test_2", 1987, 9)
        second_result = str(self.movie > movie_2)
        expected_result_2 = f'"{movie_2.name}" is better than "{self.movie.name}"'
        self.assertEqual(expected_result_2, second_result)

    def test__repr__expected_to_return_correct_result(self):
        actors = ["test1", 'test2']
        self.movie.actors = actors

        expected_result = f"Name: {self.NAME}\n" \
            f"Year of Release: {self.YEAR}\n" \
            f"Rating: {self.RATING:.2f}\n" \
            f"Cast: {', '.join(actors)}"
        actual_result = repr(self.movie)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()

