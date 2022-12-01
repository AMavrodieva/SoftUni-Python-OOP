from project_tasks.car_manager import Car


from unittest import TestCase, main


class CarManagerTests(TestCase):
    MAKE = "BMW"
    MODEL = 'E90'
    FUEL_CONSUMPTION = 7
    FUEL_CAPACITY = 60

    def setUp(self) -> None:
        self.car = Car(self.MAKE, self.MODEL, self.FUEL_CONSUMPTION, self.FUEL_CAPACITY)
        # car_1 = Car(make=VW, model=Arteon, fuel_consumption=6, fuel_capacity=50)

    def test__initialized_correctly(self):
        self.assertEqual(self.MAKE, self.car.make)
        self.assertEqual(self.MODEL, self.car.model)
        self.assertEqual(self.FUEL_CONSUMPTION, self.car.fuel_consumption)
        self.assertEqual(self.FUEL_CAPACITY, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test__empty_make_name__expect_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

        with self.assertRaises(Exception) as context:
            self.car.make = 0
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test__set_make(self):
        self.car.make = "New"
        self.assertEqual("New", self.car.make)

    def test__empty_model_name__expect_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.model = 0
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test__set_model(self):
        self.car.model = "New"
        self.assertEqual("New", self.car.model)

    def test__fuel_consumption__when_value_is_negative_or_zero_expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test__set_fuel_consumption(self):
        self.car.fuel_consumption = 5
        self.assertEqual(5, self.car.fuel_consumption)

    def test__fuel_capacity__when_value_is_negative_expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test__fuel_capacity__when_value_is_zero_expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test__set_fuel_capacity(self):
        self.car.fuel_capacity = 10
        self.assertEqual(10, self.car.fuel_capacity)

    def test__fuel_amount__when_value_is_negative_expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.car.fuel_amount = -2
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test__set_fuel_amount(self):
        self.car.fuel_amount = 10
        self.assertEqual(10, self.car.fuel_amount)

    def test__refuel_when_fuel_is_negative_or_zero_expected_to_raise_error(self):
        with self.assertRaises(Exception) as context:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))
        with self.assertRaises(Exception) as context:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test__refuel_when_fuel_is_valid__expected_correct_result(self):
        self.car.refuel(80)
        self.assertEqual(self.FUEL_CAPACITY, self.car.fuel_amount)

    def test__drive__when_needed_fuel_is_less_than_available__expected_raise_exception(self):
        self.car.refuel(0.1)
        with self.assertRaises(Exception) as context:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test__drive__when_needed_fuel_is_more_than_available__expected_fuel_amount_to_decremented(self):
        self.car.refuel(10)
        self.car.drive(50)
        self.assertEqual(6.5, self.car.fuel_amount)


if __name__ == "__main__":
    main()
