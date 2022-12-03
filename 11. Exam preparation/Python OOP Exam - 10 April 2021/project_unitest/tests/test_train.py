from project_unitest.train.train import Train
# from project_unitest.train.train import Train

from unittest import TestCase, main


class TestTrain(TestCase):
    NAME = "Train1"
    CAPACITY = 2

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertListEqual([], self.train.passengers)

    def test__add__when__capacity_is_full__expected_to_raise_exception(self):
        passenger_1, passenger_2, passenger_3 = "Pesho", "Mariya", "Petar"
        passenger_list = [passenger_1, passenger_2]
        self.train.passengers.extend(passenger_list)
        with self.assertRaises(ValueError) as context:
            self.train.add(passenger_3)
        self.assertEqual("Train is full", str(context.exception))

    def test__add__when__passenger_exist__expected_to_raise_exception(self):
        passenger_1 = "Pesho"
        self.train.passengers.append(passenger_1)
        with self.assertRaises(ValueError) as context:
            self.train.add(passenger_1)
        self.assertEqual(f"Passenger {passenger_1} Exists", str(context.exception))

    def test__add__when__there_are_capacity_and_passenger_not_exist__expected_correct_result(self):
        passenger_1 = "Pesho"
        result = self.train.add(passenger_1)
        self.assertEqual(f"Added passenger {passenger_1}", result)
        self.assertEqual([passenger_1], self.train.passengers)

    def test__remove__when_passenger_not_exist__expected_to_return_exception(self):
        passenger_1 = "Pesho"
        with self.assertRaises(ValueError) as context:
            self.train.remove(passenger_1)
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test__remove__expected_successful(self):
        passenger_1 = "Pesho"
        self.train.passengers.append(passenger_1)
        result = self.train.remove(passenger_1)
        self.assertEqual(f"Removed {passenger_1}", result)
        self.assertListEqual([], self.train.passengers)


if __name__ == "__main__":
    main()