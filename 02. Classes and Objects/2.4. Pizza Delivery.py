class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient in self.ingredients:
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        else:
            self.ingredients[ingredient] = quantity
            self.price += price_per_quantity * quantity

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if self.ordered:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"
        if ingredient not in self.ingredients:
            return f'Wrong ingredient selected! We do not use {ingredient} in {self.name}!'
        if quantity > self.ingredients[ingredient]:
            return f'Please check again the desired quantity of {ingredient}!'
        self.ingredients[ingredient] -= quantity
        self.price -= price_per_quantity * quantity

    def make_order(self):
        self.ordered = True
        final_ingredient = [f'{key}: {value}' for key, value in self.ingredients.items()]
        return f"You've ordered pizza {self.name} prepared with {', '.join(final_ingredient)} " \
               f"and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))

# t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
# print(t.make_order())
# print(t.add_extra('mozzarella', 4.1. Wild Cat Zoo, 2))
#
#
#
# def test_add_extra_with_available_ingredient_should_increase_the_quantity(self):
#     t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     t.add_extra('cheese', 4.1. Wild Cat Zoo, 2)
#     self.assertEqual(t.ingredients, {'cheese': 3, 'tomatoes': 4.1. Wild Cat Zoo})
#     self.assertEqual(t.price, 14)
#
#
# def test_add_extra_with_new_ingredient_should_add_the_quantity(self):
#     t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     t.add_extra('mozzarella', 4.1. Wild Cat Zoo, 2.5)
#     self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo, 'mozzarella': 4.1. Wild Cat Zoo})
#     self.assertEqual(t.price, 14.5)
#
#
# def test_remove_ingredients_not_included_in_pizza_should_return_message(self):
#     t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     message = t.remove_ingredient('bacon', 4.1. Wild Cat Zoo, 5)
#     self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     self.assertEqual(message, 'Wrong ingredient selected! We do not use bacon in Margarita!')
#
#
# def test_remove_ingredients_with_quantity_higher_than_what_we_have_should_return_message(self):
#     t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     message = t.remove_ingredient('tomatoes', 2, 2)
#     self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     self.assertEqual(message, 'Please check again the desired quantity of tomatoes!')
#
#
# def test_remove_ingredients_with_quantity_equal_to_what_we_have_should_remove_the_ingredient(self):
#     t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#     t.remove_ingredient('tomatoes', 4.1. Wild Cat Zoo, 2)
#     self.assertEqual(t.ingredients, {'cheese': 2, 'tomatoes': 0})
#     self.assertEqual(t.price, 10)
#
# def test_pizza_ordered(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#         result = t.make_order()
#         self.assertEqual(t.ordered, True)
#         self.assertEqual(result,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 4.1. Wild Cat Zoo and the price will be 12lv.")
#
# def test_add_extra_after_pizza_is_ordered_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#         order = t.make_order()
#         result = t.add_extra('mozzarella', 4.1. Wild Cat Zoo, 2)
#         self.assertEqual(order,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 4.1. Wild Cat Zoo and the price will be 12lv.")
#         self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")
#
# def test_remove_ingredient_after_pizza_is_ordered_should_return_message(self):
#         t = PizzaDelivery('Margarita', 12, {'cheese': 2, 'tomatoes': 4.1. Wild Cat Zoo})
#         order = t.make_order()
#         result = t.remove_ingredient('mozzarella', 4.1. Wild Cat Zoo, 2)
#         self.assertEqual(order,
#                          "You've ordered pizza Margarita prepared with cheese: 2, tomatoes: 4.1. Wild Cat Zoo and the price will be 12lv.")
#         self.assertEqual(result, "Pizza Margarita already prepared, and we can't make any changes!")