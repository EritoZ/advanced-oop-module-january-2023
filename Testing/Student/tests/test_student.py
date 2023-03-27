import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        self.student = Student('X AE A-XII', {'math': ['???']})

    def test_enroll_course_already_added(self):
        result = self.student.enroll('math', ['???...'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({'math': ['???', '???...']}, self.student.courses)

    def test_enroll_course_and_course_notes_added_with_blank(self):
        result = self.student.enroll('idk man', ['???'])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'math': ['???'], 'idk man': ['???']}, self.student.courses)

    def test_enroll_course_and_course_notes_added_with_Y(self):
        result = self.student.enroll('idk man', ['???'], 'Y')

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({'math': ['???'], 'idk man': ['???']}, self.student.courses)

    def test_enroll_course_and_course_notes_added_with_smt_else(self):
        result = self.student.enroll('idk man', ['???'], 'Ga')

        self.assertEqual("Course has been added.", result)
        self.assertEqual({'math': ['???'], 'idk man': []}, self.student.courses)

    def test_add_notes_updated(self):
        result = self.student.add_notes('math', 'gagaga')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual({'math': ['???', 'gagaga']}, self.student.courses)

    def test_add_notes_error(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes('maasdsa', 'gagaga')

        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_leave_course_removed(self):
        result = self.student.leave_course('math')

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_course_error(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course('maasdsa')

        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))
