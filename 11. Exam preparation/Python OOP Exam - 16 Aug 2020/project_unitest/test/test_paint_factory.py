from project_unitest.factory.factory import Factory
from project_unitest.factory.paint_factory import PaintFactory
from unittest import TestCase, main


class TestPaintFactory(TestCase):
    NAME = "Factory"
    CAPACITY = 10
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]
    INGREDIENTS = {}
    CLASS_NAME = PaintFactory.__name__

    def setUp(self) -> None:
        self.paint_factory = PaintFactory(self.NAME, self.CAPACITY)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.paint_factory.name)
        self.assertEqual(self.CAPACITY, self.paint_factory.capacity)
        self.assertDictEqual({}, self.paint_factory.ingredients)
        self.assertEqual(self.VALID_INGREDIENTS, self.paint_factory.valid_ingredients)
        self.assertEqual(self.INGREDIENTS, self.paint_factory.products)

    def test__add_ingredient__invalid_product_type__expected_raise_exception(self):
        product_type = 'black'
        with self.assertRaises(TypeError) as context:
            self.paint_factory.add_ingredient(product_type, 10)
        expected_error = f"Ingredient of type {product_type} not allowed in {self.CLASS_NAME}"
        self.assertEqual(expected_error, str(context.exception))

    def test__add_ingredient__not_enough_space_invalid_can_add__expected_raise_exception(self):
        product_type = 'white'
        with self.assertRaises(ValueError) as context:
            self.paint_factory.add_ingredient(product_type, 15)
        expected_error = "Not enough space in factory"
        self.assertEqual(expected_error, str(context.exception))

    def test__can_add__expected_correct_result(self):
        quantity_1, quantity_2 = 5, 15
        self.assertEqual(False, self.paint_factory.can_add(quantity_2))
        self.assertEqual(True, self.paint_factory.can_add(quantity_1))

    def test__add_ingredient__valid_value__expected_correct_result(self):
        self.paint_factory.capacity = 100
        product_type, quantity = 'white', 15
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.add_ingredient(product_type, quantity)
        self.assertEqual(30, sum(self.paint_factory.ingredients.values()))
        self.assertEqual({'white': 30}, self.paint_factory.ingredients)

    def test__remove_ingredient__invalid_product_type__expected_to_raise_exception(self):
        product_type = 'black'
        with self.assertRaises(KeyError) as context:
            self.paint_factory.remove_ingredient(product_type, 10)
        expected_error = """'No such ingredient in the factory'"""
        self.assertEqual(expected_error, str(context.exception))

    def test__remove_ingredients__not_enough_quantity__expected_to_raise_exception(self):
        self.paint_factory.capacity = 100
        product_type, quantity = 'white', 15
        self.paint_factory.add_ingredient(product_type, quantity)
        with self.assertRaises(ValueError) as context:
            self.paint_factory.remove_ingredient(product_type, 20)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(context.exception))

    def test__remove_ingredient__valid_value__expected_correct_result(self):
        self.paint_factory.capacity = 100
        product_type, quantity = 'white', 15
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.remove_ingredient(product_type, 10)
        self.assertEqual(5, self.paint_factory.ingredients[product_type])

    def test__repr__without_ingredient__expected_correct_result(self):
        expected_result = f"""Factory name: {self.NAME} with capacity {self.CAPACITY}.
"""
        actual = repr(self.paint_factory)
        self.assertEqual(expected_result, actual)

    def test__repr__with_ingredient__expected_correct_result(self):
        self.paint_factory.capacity = 100
        product_type, quantity = 'white', 15
        product_type_1, quantity_1 = "yellow", 10
        self.paint_factory.add_ingredient(product_type, quantity)
        self.paint_factory.add_ingredient(product_type_1, quantity_1)
        expected_result = f"""Factory name: {self.NAME} with capacity {self.paint_factory.capacity}.
{product_type}: {quantity}
{product_type_1}: {quantity_1}
"""
        actual = repr(self.paint_factory)
        self.assertEqual(expected_result, actual)


if __name__ == "__main__":
    main()