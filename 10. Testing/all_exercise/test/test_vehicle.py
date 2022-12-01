from all_exercise.project.vehicle import Vehicle
# for test in system
# from project.vehicle import Vehicle

from unittest import TestCase, main


class TestVehicle(TestCase):
    FUEL = 60
    CAPACITY = 60
    HORSE_POWER = 100
    FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test__initialized_correctly(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.CAPACITY, self.vehicle.capacity)
        self.assertEqual(self.FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test__drive__when_fuel_is_not_enough__expected_to_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test__drive_when_distance_is_reachable__expected_fuel_to_decremented(self):
        self.vehicle.drive(10)
        self.assertEqual(self.FUEL-12.50, self.vehicle.fuel)

    def test__refuel__when_fuel_is_more_than_capacity__expected_to_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(context.exception))

    def test__refuel__when_there_is_capacity__expected_fuel_incremented(self):
        self.vehicle.drive(20)
        self.vehicle.refuel(10)
        self.assertEqual(45, self.vehicle.fuel)

    def test__str__expected_return_correct_string(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.FUEL_CONSUMPTION} fuel consumption"
        actual_result = str(self.vehicle)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
