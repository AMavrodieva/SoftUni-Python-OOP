from all_exercise.project.student import Student

# use follow when submit to judge
# from project.student import Student

from unittest import TestCase, main


class TestStudent(TestCase):
    NAME = "Student_1"

    def setUp(self) -> None:
        self.student = Student(self.NAME)

    def test__initialized_correctly__without_courses(self):
        student = Student(self.NAME)
        self.assertEqual(self.NAME, student.name)
        self.assertEqual({}, student.courses)

    def test__initialized_correctly__with_courses(self):
        courses = {"Python": ['note_1', 'note_2']}
        student = Student(self.NAME, courses)
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(courses, student.courses)

    def test__enroll__when_course_is_in_courses__expected_to_update_notes(self):
        course_name = "Python"
        courses = {course_name: ['note_1', 'note_2']}
        student = Student(self.NAME, courses)
        result = student.enroll(course_name, ["note_3", 'note_4'])
        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note_1', 'note_2', "note_3", 'note_4'], student.courses[course_name])

    def test__enroll__when_added_note_is_passed__expected_to_update_courses_and_notes(self):
        course_name = "Python_OOP"
        notes = ['note_1', 'note_2']

        result = self.student.enroll(course_name, notes, "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['note_1', 'note_2'], self.student.courses[course_name])

    def test__enroll__when_added_notes_is_passed__expected_to_update_courses_and_notes(self):
        course_name = "Python_OOP"
        notes = ['note_1', 'note_2']
        result = self.student.enroll(course_name, notes)
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(['note_1', 'note_2'], self.student.courses[course_name])

    def test__enroll__when_added_note_is_invalid__expected_to_add_course_without_notes(self):
        course_name = "Python_OOP"
        notes = ['note_1', 'note_2']
        result = self.student.enroll(course_name, notes, "P")
        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes__when_course_not_in_courses__expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.add_notes("Python_Advanced", ["note_1, note_2"])
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_add_notes__when_course_in_courses__expected_notes_to_incremented(self):
        course_name = "Python_OOP"
        notes = ['note_1', 'note_2']
        courses = {course_name: notes}
        student = Student(self.NAME, courses)
        result = student.add_notes(course_name, "note_3")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note_1', 'note_2', "note_3"], student.courses[course_name])

    def test_leave_course__when_course_not_in_courses__expected_raise_exception(self):
        with self.assertRaises(Exception) as context:
            self.student.leave_course("Python")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_leave_course__when_course_in_courses__expected_notes_to_incremented(self):
        course_name = "Python_OOP"
        notes = ['note_1', 'note_2']
        courses = {course_name: notes, "Python_Advanced": notes}
        student = Student(self.NAME, courses)
        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in courses)


if __name__ == "__main__":
    main()
