
# from project_unitest.student_report_card import StudentReportCard
from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class TestStudentReportCard(TestCase):
    STUDENT_NAME = "Mariya"
    SCHOOL_YEAR = 4

    def setUp(self) -> None:
        self.student_card = StudentReportCard(self.STUDENT_NAME, self.SCHOOL_YEAR)

    def test__initialized_correctly(self):
        self.assertEqual(self.STUDENT_NAME, self.student_card.student_name)
        self.assertEqual(self.SCHOOL_YEAR, self.student_card.school_year)
        self.assertDictEqual({}, self.student_card.grades_by_subject)

    def test__set_name__expected_correct_result(self):
        self.student_card.student_name = "Pesho"
        self.assertEqual("Pesho", self.student_card.student_name)

    def test__set_name__invalid_name__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.student_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))

    def test__set_school_year__expected_correct_result(self):
        self.student_card.school_year = 1
        self.assertEqual(1, self.student_card.school_year)
        self.student_card.school_year = 12
        self.assertEqual(12, self.student_card.school_year)

    def test__set_school_year__invalid_year_must_be_between_1_12__expected_to_raise_exception(self):
        with self.assertRaises(ValueError) as context:
            self.student_card.student_name = ""
        self.assertEqual("Student Name cannot be an empty string!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.student_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.student_card.school_year = -1
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        with self.assertRaises(ValueError) as context:
            self.student_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(context.exception))
        with self.assertRaises(TypeError):
            self.student_card.school_year = "1"

    def test__add_grade__expected_to_return_correct_result(self):
        subject = "Math"
        grade = 5.5
        self.student_card.add_grade(subject, grade)
        self.assertEqual({subject: [grade]}, self.student_card.grades_by_subject)

    def test__add_grade__when_subject_is_available_expected_to_return_correct_result(self):
        subject = "Math"
        grade_1, grade_2 = 5.5, 4.5
        self.student_card.add_grade(subject, grade_1)
        self.student_card.add_grade(subject, grade_2)
        self.assertEqual({subject: [grade_1, grade_2]}, self.student_card.grades_by_subject)

    def test__average_grade__expected_to_raise_exception(self):
        subject = "Math"
        self.student_card.grades_by_subject[subject] = []
        with self.assertRaises(Exception):
            self.student_card.average_grade_by_subject()

    def test__average_grade_be_subject__expected_correct_info(self):
        subject_1, grade_1 = "Math", 5.5
        subject_2, grade_2, grade_21 = "English", 4.5, 5.0
        self.student_card.add_grade(subject_1, grade_1)
        self.student_card.add_grade(subject_2, grade_2)
        self.student_card.add_grade(subject_2, grade_21)
        expected_result = f"""{subject_1}: 5.50
{subject_2}: 4.75"""
        actual = self.student_card.average_grade_by_subject()
        self.assertEqual(expected_result, actual)
        self.assertIn(subject_1, self.student_card.grades_by_subject)
        self.assertIn(subject_2, self.student_card.grades_by_subject)
        self.assertListEqual([grade_1], self.student_card.grades_by_subject[subject_1])
        self.assertListEqual([grade_2, grade_21], self.student_card.grades_by_subject[subject_2])

    def test__average_grade_for_all__expected_to_raise_exception(self):
        subject = "Math"
        self.student_card.grades_by_subject[subject] = []
        with self.assertRaises(Exception):
            self.student_card.average_grade_for_all_subjects()

    def testt__average_grade_for_all_subjects__expected_correct_info(self):
        subject_1, grade_1 = "Math", 5.5
        subject_2, grade_2, grade_21 = "English", 4.5, 5.0
        self.student_card.add_grade(subject_1, grade_1)
        self.student_card.add_grade(subject_2, grade_2)
        self.student_card.add_grade(subject_2, grade_21)
        expected_result = f"""Average Grade: 5.00"""
        actual = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(expected_result, actual)

    def test__repr__expected_correct_result(self):
        subject_1, grade_1 = "Math", 5.5
        subject_2, grade_2, grade_21 = "English", 4.5, 5.0
        self.student_card.add_grade(subject_1, grade_1)
        self.student_card.add_grade(subject_2, grade_2)
        self.student_card.add_grade(subject_2, grade_21)
        expected_result = f"""Name: {self.STUDENT_NAME}
Year: {self.SCHOOL_YEAR}
----------
{subject_1}: 5.50
{subject_2}: 4.75
----------
Average Grade: 5.00"""

        actual = repr(self.student_card)
        self.assertEqual(expected_result, actual)


if __name__ == "__main__":
    main()
