#from Student import Student
from datetime import datetime
#from Course import Course
class Enrollment:
    def __init__(self, EnrollmentID, StudentID, CourseID, EnrollmentDate):
        self._EnrollmentID = EnrollmentID
        self._StudentID = StudentID
        self._CourseID = CourseID
        self._EnrollmentDate = EnrollmentDate

    def __init__(self, db_connector):
        self._db_connector = db_connector

    @property
    def EnrollmentID(self):
        return self._EnrollmentID

    @EnrollmentID.setter
    def EnrollmentID(self, new_EnrollmentID):
        if isinstance(new_EnrollmentID, int) and new_EnrollmentID > 0:
            self._EnrollmentID = new_EnrollmentID
        else:
            raise ValueError("Enrollment ID must be a positive integer.")

    @property
    def StudentID(self):
        return self._StudentID

    @StudentID.setter
    def StudentID(self, new_StudentID):
        if isinstance(new_StudentID, int) and new_StudentID > 0:
            self._StudentID = new_StudentID
        else:
            raise ValueError("Student ID must be a positive integer.")

    @property
    def CourseID(self):
        return self._CourseID

    @CourseID.setter
    def CourseID(self, new_CourseID):
        if isinstance(new_CourseID, int) and new_CourseID > 0:
            self._CourseID = new_CourseID
        else:
            raise ValueError("Course ID must be a positive integer.")

    @property
    def EnrollmentDate(self):
        return self._EnrollmentDate

    @EnrollmentDate.setter
    def EnrollmentDate(self, new_EnrollmentDate):
        if isinstance(new_EnrollmentDate, str) and len(new_EnrollmentDate) == 10:
            self._EnrollmentDate = new_EnrollmentDate
        else:
            raise ValueError("Invalid enrollment date format.")

    def GetStudents(self):
        return self._enrollments

    '''
student_1 = Student(StudentID=1, FirstName="Pradip", LastName="Bochare", DateOfBirth=datetime(2002, 8, 3), Email="pradip@email.com", PhoneNumber="1234567890")
student_2 = Student(StudentID=2, FirstName="Abhishek", LastName="Zune", DateOfBirth=datetime(2001, 2, 2), Email="abhishek@email.com", PhoneNumber="9876543210")

python_course = Course(101, "Python", "202", "Anjali")
student_1.EnrollInCourse(python_course)
student_2.EnrollInCourse(python_course)

enrollments= python_course.GetEnrollments()

print("Enrolled Students:")
for student in enrollments:
    print(f"- Student ID: {student.StudentID}, Student Name: {student.FirstName} {student.LastName}")
    '''

    # TASK 9
    def Enroll_Course(self, enrollment_id, student_id, course_id):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO enrollments (enrollment_id, student_id, course_id, enrollemnt_date) VALUES (%s, %s, %s,%s)"
            values = (enrollment_id, student_id, course_id, datetime.now())

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            course_name_query = "SELECT course_name FROM course WHERE course_id=%s"
            values_query = (course_id,)
            with self._db_connector.connection.cursor() as cursor1:
                cursor1.execute(course_name_query, values_query)
                c_name = cursor1.fetchone()
            self._db_connector.connection.commit()
            if c_name:
                print(f"John enrolled in course named {c_name[0]} successfully.")

        except Exception as e:
            print(f"Error enrolling course: {e}")

        finally:
            self._db_connector.close_connection()

    # TASK 11
    def retrieve_enrollment_record(self, course_id):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM enrollments where course_id=%s"
            values = (course_id,)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                enrollment_details = cursor.fetchall()
                if enrollment_details:
                    print("Enrollment details:")
                    for enroll in enrollment_details:
                        print(f"Enrollment ID:{enroll[0]}")
                        print(f"Student ID:{enroll[1]}")
                        print(f"Enrollment Date:{enroll[3]}")
                else:
                    print("no enrollments found.")

            self._db_connector.connection.commit()
        except Exception as e:
            print(f"Error getting enrollment details: {e}")
        finally:
            self._db_connector.close_connection()

    def retrieve_studentenroll_course_record(self, course_id):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM enrollments where course_id=%s"
            values = (course_id,)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                enrollment_details = cursor.fetchall()
                if enrollment_details:
                    print("Enrollment details:")
                    for enroll in enrollment_details:
                        print(f"Enrollment ID:{enroll[0]}")
                        print(f"Student ID:{enroll[1]}")
                        print(f"Enrollment Date:{enroll[3]}")
                else:
                    print("no enrollments found.")

            self._db_connector.connection.commit()
        except Exception as e:
            print(f"Error getting enrollment details: {e}")
        finally:
            self._db_connector.close_connection()

