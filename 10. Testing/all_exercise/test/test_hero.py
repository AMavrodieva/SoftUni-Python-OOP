from all_exercise.project.hero import Hero

# from project.hero import Hero

from unittest import TestCase, main


class TestHero(TestCase):
    PLAYER_USERNAME = "Attacker"
    PLAYER_LEVEL = 10
    PLAYER_HEALTH = 100
    PLAYER_DAMAGE = 50

    def setUp(self) -> None:
        self.player = Hero(self.PLAYER_USERNAME, self.PLAYER_LEVEL, self.PLAYER_HEALTH, self.PLAYER_DAMAGE)

    def test__initialized_correctly(self):
        self.assertEqual(self.PLAYER_USERNAME, self.player.username)
        self.assertEqual(self.PLAYER_LEVEL, self.player.level)
        self.assertEqual(self.PLAYER_HEALTH, self.player.health)
        self.assertEqual(self.PLAYER_DAMAGE, self.player.damage)

    def test__battle_when_second_player_has_same_username_expected_to_raise_exception(self):
        enemy = Hero(self.PLAYER_USERNAME, 5, 70, 40)
        with self.assertRaises(Exception) as context:
            self.player.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test__battle_when_player_health_is_zero_or_negative_expected_to_raise_exception(self):
        enemy = Hero("Enemy", 5, 70, 40)
        with self.assertRaises(ValueError) as context:
            self.player.health = 0
            self.player.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.player.health = -1
            self.player.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test__battle_when_other_player_health_is_zero_or_negative_expected_to_raise_exception(self):
        enemy = Hero("Enemy", 5, 0, 40)
        with self.assertRaises(ValueError) as context:
            self.player.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(context.exception))
        enemy_1 = Hero("Enemy", 5, -1, 40)
        with self.assertRaises(ValueError) as context:
            self.player.battle(enemy_1)
        self.assertEqual(f"You cannot fight {enemy_1.username}. He needs to rest", str(context.exception))

    def test__battle__when_two_player_died_expected_to_return_correctly_string(self):
        enemy = Hero("Enemy", 5, 80, 40)
        result = self.player.battle(enemy)
        self.assertEqual("Draw", result)

    def test__battle__when_player_win_to_return_correctly_string(self):
        enemy = Hero("Enemy", 5, 80, 10)
        result = self.player.battle(enemy)
        self.assertEqual("You win", result)

    def test__battle__when_player_win__expected_player_gets_prizes(self):
        enemy = Hero("Enemy", 5, 80, 10)
        enemy_damage = enemy.damage * enemy.level
        self.player.battle(enemy)
        self.assertEqual(self.PLAYER_LEVEL + 1, self.player.level)
        self.assertEqual(self.PLAYER_HEALTH - enemy_damage + 5, self.player.health)
        self.assertEqual(self.PLAYER_DAMAGE + 5, self.player.damage)

    def test__battle__when_other_player_win_to_return_correctly_string(self):
        enemy = Hero("Enemy", 15, 600, 60)
        result = self.player.battle(enemy)
        self.assertEqual("You lose", result)

    def test__battle__when_other_player_win__expected_other_player_gets_prizes(self):
        enemy = Hero("Enemy", 15, 600, 60)
        player_damage = self.PLAYER_DAMAGE * self.PLAYER_LEVEL
        self.player.battle(enemy)
        self.assertEqual(15 + 1, enemy.level)
        self.assertEqual(600 - player_damage + 5, enemy.health)
        self.assertEqual(60 + 5, enemy.damage)

    def test__str__expected_correct_string(self):
        actual_result = str(self.player)
        expected_result = f"Hero {self.PLAYER_USERNAME}: {self.PLAYER_LEVEL} lvl\n" \
               f"Health: {self.PLAYER_HEALTH}\n" \
               f"Damage: {self.PLAYER_DAMAGE}\n"
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
