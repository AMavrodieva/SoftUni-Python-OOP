from project_tasks.worker import Worker
"""
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called
•	Test if the get_info method returns the proper string with correct values
"""


from unittest import TestCase, main


class WorkerTests(TestCase):
    NAME = "Djery"
    SALARY = 1500
    ENERGY = 2

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test__init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test__rest__expected_energy_to_incremented(self):
        self.worker.rest()
        self.assertEqual(self.ENERGY + 1, self.worker.energy)

    def test__work__when_energy_less_than_0_expect_raise_exception(self):
        worker = Worker(self.NAME, self.SALARY, 0)
        with self.assertRaises(Exception) as error:
            worker.work()
        self.assertEqual('Not enough energy.', str(error.exception))

    def test__work__when_enough_energy__expected_salary_to_incremented(self):
        self.worker.work()
        self.worker.work()
        self.assertEqual(2 * self.SALARY, self.worker.money)

    def test__work__when_enough_energy_expected_energy_to_decremented(self):
        self.worker.work()
        self.assertEqual(self.ENERGY - 1, self.worker.energy)

    def test__get_info__expected_proper_string(self):
        result = self.worker.get_info()
        self.assertEqual(f'{self.NAME} has saved {0} money.', result)


if __name__ == '__main__':
    main()
