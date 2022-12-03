# from project_unitest.team import Team

from project_unitest.team import Team

from unittest import TestCase, main


class TestTeam(TestCase):
    NAME = "Team"

    def setUp(self) -> None:
        self.team = Team(self.NAME)

    def test__initialized_correctly(self):
        self.assertEqual(self.NAME, self.team.name)
        self.assertDictEqual({}, self.team.members)

    def test__set_name__invalid_value__expected_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.team.name = "5"
        self.assertEqual("Team Name can contain only letters!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.team.name = "as5"
        self.assertEqual("Team Name can contain only letters!", str(context.exception))

    def test__add_number__expected_correct_result(self):
        self.team.members['Ivan'] = 18
        name_3, name_1, name_2 = "Ivan", "Mariya", "Gosho"
        result = self.team.add_member(Ivan=17, Mariya=10, Gosho=15)
        expected_result = f"Successfully added: {name_1}, {name_2}"
        self.assertEqual(expected_result, result)
        self.assertEqual(18, self.team.members[name_3])
        self.assertEqual(10, self.team.members[name_1])
        self.assertEqual(15, self.team.members[name_2])

    def test__remove_member__when_member_exist__expected_to_return_correct_str(self):
        name_1, name_2 = "Mariya", "Gosho"
        self.team.members[name_1] = 18
        self.team.members[name_2] = 21
        result = self.team.remove_member(name_1)
        expected_result = f"Member {name_1} removed"
        self.assertEqual(expected_result, result)
        self.assertNotIn(name_1, self.team.members)

    def test__remove_member__when_member_not_exist__expected_to_return_correct_str(self):
        name_1, name_2, name_3 = "Mariya", "Gosho", "Pesho"
        self.team.members[name_1] = 18
        self.team.members[name_2] = 21
        result = self.team.remove_member(name_3)
        expected_result = f"Member with name {name_3} does not exist"
        self.assertEqual(expected_result, result)

    def test__gt__expected_correct_result(self):
        name_1, name_2, name_3, name_4 = "Mariya", "Gosho", "Pesho", "Vasil"
        self.team.members[name_1] = 10
        self.team.add_member(name_2=20, name_3=15)
        team2 = Team("TeamSecond")
        team2.add_member(name_2=20, name_3=15)
        team3 = Team("TeamThird")
        team3.add_member(name_2=20, name_3=15, name_4=20)
        self.assertEqual(True, self.team > team2)
        self.assertEqual(False, self.team > team3)

    def test__len__expected_to_return_correct_value(self):
        name_1, name_2 = "Mariya", "Gosho"
        self.team.members[name_1] = 10
        self.team.members[name_2] = 20
        actual = len(self.team)
        self.assertEqual(2, actual)

    def test__add__expected_correct_result(self):
        name_1, name_2 = "Mariya", "Gosho"
        self.team.members[name_1] = 18
        team_name = "TeamSecond"
        team2 = Team(team_name)
        team2.members[name_2] = 21
        result = self.team + team2
        exp_name = f'{self.NAME}{team_name}'
        expected_team_members = {name_1: 18, name_2: 21}
        self.assertEqual(exp_name, result.name)
        self.assertEqual(expected_team_members, result.members)

    def test__str__expected_correct_str(self):
        name_1, name_2 = "Mariya", "Gosho"
        self.team.members[name_1] = 20
        self.team.members[name_2] = 15
        expected_result = f"""Team name: {self.NAME}
Member: {name_1} - {self.team.members[name_1]}-years old
Member: {name_2} - {self.team.members[name_2]}-years old"""
        actual_result = str(self.team)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
