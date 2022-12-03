from project_unitest.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):
    SIZE = 10

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test__initialized_correctly(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertDictEqual({}, self.plantation.plants)
        self.assertListEqual([], self.plantation.workers)

    def test__set_size__when_value_is_negative__expected_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(context.exception))

    def test__set_size__when_value_is_correct__expected_correct_result(self):
        self.plantation.size = 5
        self.assertEqual(5, self.plantation.size)

    def test__hire_worker__when_value_is_already_hired_expected_raise_error(self):
        worker_1 = "Test1"
        workers_list = [worker_1, "Test2", "Test3"]
        self.plantation.workers.extend(workers_list)
        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker(worker_1)
        self.assertEqual("Worker already hired!", str(context.exception))

    def test__hire_worker__expected_correct_result(self):
        worker_1 = "Test1"
        result = self.plantation.hire_worker(worker_1)
        self.assertEqual(f"{worker_1} successfully hired.", result)
        self.assertIn(worker_1, self.plantation.workers)

    def test__len__expected_return_correct_value(self):
        plant_1, plant_2 = "rose", "cucumber"
        plants_planted = {"Test1": plant_1, "Test2": plant_2}
        self.plantation.plants = plants_planted
        expected_result = len(plant_1) + len(plant_2)
        actual_result = self.plantation.__len__()
        self.assertEqual(expected_result, actual_result)

    def test__planting__expected_to_raise_exception(self):
        plants_planted = {"Test1": "rose", "Test2": "cucumber"}
        self.plantation.plants = plants_planted
        self.plantation.workers = ["Test1", "Test2"]
        worker = "Test3"
        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, "")
        self.assertEqual(f"Worker with name {worker} is not hired!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.plantation.planting("Test1", "tomato")
        self.assertEqual("The plantation is full!", str(context.exception))

    def test__planting__when_worker_already_have_worked_at_plant_expected_to_return_new_plant(self):
        self.plantation.size = 100
        worker, plant_1, plant_2 = "Test1", "plant1", "plant2"
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant_1)
        result = self.plantation.planting(worker, plant_2)
        self.assertEqual(f"{worker} planted {plant_2}.", result)
        self.assertEqual({worker: [plant_1, plant_2]}, self.plantation.plants)

    def test__planting__when_worker_is_not_worked_at_plant_expected_element_in_plants_to_incremented(self):
        self.plantation.size = 100
        worker_1, plant = "Test2", "tomato"
        self.plantation.hire_worker(worker_1)
        result = self.plantation.planting(worker_1, plant)
        self.assertEqual(f"{worker_1} planted it's first {plant}.", result)
        self.assertEqual({worker_1: [plant]}, self.plantation.plants)

    def test__str__when_no_workers_expected_correct_result(self):
        expected_result = f"""Plantation size: {self.SIZE}
"""
        actual = str(self.plantation)
        self.assertEqual(expected_result, actual)

    def test__str_when_workers_no_plants__expected_correct_result(self):
        workers = ["Test_1", "Test2"]
        [self.plantation.hire_worker(w) for w in workers]
        expected_result = f"""Plantation size: {self.SIZE}
Test_1, Test2"""
        actual = str(self.plantation)
        self.assertEqual(expected_result, actual)

    def test__str_when_workers_and_plants__expected_correct_result(self):
        workers = ["Test_1", "Test2"]
        plants = ['plant1', 'plant2']
        plants_2 = ['plant1', 'plant2', 'plant3']
        [self.plantation.hire_worker(w) for w in workers]
        [self.plantation.planting(workers[0], pl) for pl in plants]
        [self.plantation.planting(workers[1], pl) for pl in plants_2]
        expected_result = f"""Plantation size: {self.SIZE}
Test_1, Test2
Test_1 planted: {", ".join(plants)}
Test2 planted: {", ".join(plants_2)}"""
        actual = str(self.plantation)
        self.assertEqual(expected_result, actual)

    def test__repr__no_worker__expected_correct_result(self):
        expected_result = f"""Size: {self.SIZE}
Workers: """
        actual_result = repr(self.plantation)
        self.assertEqual(expected_result, actual_result)

    def test__repr__with_worker__expected_correct_result(self):
        workers = ["Test_1", "Test2"]
        [self.plantation.hire_worker(w) for w in workers]
        expected_result = f"""Size: {self.SIZE}
Workers: {", ".join(workers)}"""
        actual_result = repr(self.plantation)
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()