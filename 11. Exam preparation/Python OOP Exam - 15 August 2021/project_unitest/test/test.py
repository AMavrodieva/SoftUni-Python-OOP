from project_unitest.pet_shop import PetShop

from unittest import TestCase, main


class TestPetShop(TestCase):
    NAME = "My Pet Shop"

    def setUp(self) -> None:
        self.petshop = PetShop(self.NAME)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.petshop.name)
        self.assertDictEqual({}, self.petshop.food)
        self.assertListEqual([], self.petshop.pets)

    def test__add_food__when_quantity_is_zero_or_negative__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.petshop.add_food("some_food", 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.petshop.add_food("some_food", -1)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(context.exception))

    def test__add_food__when_quantity_is_valid__expected_correct_str_and_add_values_at_dict_food(self):
        food, quantity = "some_food", 5
        result = self.petshop.add_food(food, quantity)
        expected_result = f"Successfully added {quantity:.2f} grams of {food}."
        self.assertEqual(expected_result, result)
        self.assertEqual({food: quantity}, self.petshop.food)

    def test__add_pet__when_pet_name_already_add_to_list_of_pets__expected_to_raise_exception(self):
        pet_name = "Djery"
        self.petshop.add_pet(pet_name)
        with self.assertRaises(Exception) as context:
            self.petshop.add_pet(pet_name)
        self.assertEqual("Cannot add a pet with the same name", str(context.exception))

    def test__add_pet__when_pet_name_not_exist__expected_to_add_pet_in_pets_list(self):
        pet_name = "Djery"
        result = self.petshop.add_pet(pet_name)
        self.assertEqual(f"Successfully added {pet_name}.", result)
        self.assertEqual([pet_name], self.petshop.pets)

    def test__feed_pet__when_pet_name_is_not_exist__expected_to_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.petshop.feed_pet("some_food", "Djery")
        self.assertEqual("Please insert a valid pet name", str(context.exception))

    def test__feed_pet__when_food_name_is_not_exist__expected_to_return_correct_str(self):
        food = "some food"
        pet_name = "Djery"
        self.petshop.pets.append(pet_name)
        result = self.petshop.feed_pet(food, pet_name)
        self.assertEqual(f"You do not have {food}", result)

    def test__feed_pet__when_food_and_pet_are_valid_and_quantity_food_less_than_100__expected_to_incremented_food(self):
        food_name = "some food"
        pet_name = "Djery"
        self.petshop.pets.append(pet_name)
        self.petshop.food[food_name] = 90
        result = self.petshop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual(1090, self.petshop.food[food_name])

    def test__feed_pet__when_food_and_pet_are_valid_and_quantity_food_is_more_than_100__expected_to_decremented_food(self):
        food_name = "some food"
        pet_name = "Djery"
        self.petshop.pets.append(pet_name)
        self.petshop.food[food_name] = 120
        result = self.petshop.feed_pet(food_name, pet_name)
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(20, self.petshop.food[food_name])

    def test__repr__when_have_not_pets(self):
        expected_result = f"""Shop {self.NAME}:
Pets: """
        actual = repr(self.petshop)
        self.assertEqual(expected_result, actual)

    def test__repr__when_there_are_pets(self):
        pet_name_1, pet_name_2 = "Djeri", "Tobi"
        self.petshop.pets.append(pet_name_1)
        self.petshop.pets.append(pet_name_2)
        expected_result = f"""Shop {self.NAME}:
Pets: {pet_name_1}, {pet_name_2}"""
        actual = repr(self.petshop)
        self.assertEqual(expected_result, actual)


if __name__ == "__main__":
    main()
