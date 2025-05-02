import pytest
from lib.enrollment import Student, Course, Enrollment

class TestCodegrade:

    def test_course_count(self):
        student = Student("Test Student")
        course1 = Course("Course 1")
        course2 = Course("Course 2")

        student.enroll(course1)
        student.enroll(course2)

        assert student.course_count() == 2

    def test_aggregate_enrollments_per_day(self):
        # Clear any existing enrollments from previous tests
        Enrollment.all.clear()

        student1 = Student("Student 1")
        student2 = Student("Student 2")
        course = Course("Course A")

        student1.enroll(course)
        student2.enroll(course)

        enrollment_data = Enrollment.aggregate_enrollments_per_day()
        assert len(enrollment_data) == 1  # One unique date
        assert list(enrollment_data.values())[0] == 2  # Two enrollments
