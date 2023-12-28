from Entity.Teacher import Teacher
from Entity.Student import Student
from Entity.Enrollment import Enrollment
from datetime import datetime
class Course:
    def __init__(self, CourseID, CourseName, CourseCode, InstructorName):
        self._CourseID = CourseID
        self._CourseName = CourseName
        self._CourseCode = CourseCode
        self._InstructorName = InstructorName
        self._enrollments = []
        #self._assigned_teacher = None

    def __init__(self, db_connector):
        self._db_connector = db_connector

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
    def CourseName(self):
        return self._CourseName

    @CourseName.setter
    def CourseName(self, new_CourseName):
        if isinstance(new_CourseName, str) and new_CourseName:
            self._CourseName = new_CourseName
        else:
            raise ValueError("Course name must be a non-empty string.")

    @property
    def CourseCode(self):
        return self._CourseCode

    @CourseCode.setter
    def CourseCode(self, new_CourseCode):
        if isinstance(new_CourseCode, str) and new_CourseCode:
            self._CourseCode = new_CourseCode
        else:
            raise ValueError("Course code must be a non-empty string.")

    @property
    def InstructorName(self):
        return self._InstructorName

    @InstructorName.setter
    def InstructorName(self, new_InstructorName):
        if isinstance(new_InstructorName, str) and new_InstructorName:
            self._InstructorName = new_InstructorName
        else:
            raise ValueError("Instructor name must be a non-empty string.")

    def AssignTeacher(self, teacher):
        self._assigned_teacher = teacher
        print(f"Teacher {teacher.FirstName} {teacher.LastName} assigned to the course {self.CourseName}.")

    """
python_teacher = Teacher(1,"Anjali", "Bhalchandra","bhalchandra@gmail.com")

python_course = Course(101, "Python",202,"Anjali")

python_course.AssignTeacher(python_teacher)
     """

    def UpdateCourseInfo(self, courseid, courseName, courseCode, instructor):
        self.CourseID = courseid
        self.CourseName = courseName
        self.CourseCode = courseCode
        self.InstructorName = instructor
        print("Course information updated successfully.")
        """
python_course = Course(101, "Python","202","Anjali")

python_course.UpdateCourseInfo(101,"Python+Pyunit", "102","Prof.Anjali")
        """

    def DisplayCourseInfo(self):
        print(f"Course ID: {self.CourseID}")
        print(f"Course Code: {self.CourseCode}")
        print(f"Course Name: {self.CourseName}")
        print(f"Instructor: {self.InstructorName}")

    """
python_course = Course(101, "Python", "202", "Anjali")
python_course.DisplayCourseInfo()
    """

    def GetEnrollments(self):
        return self._enrollments

    """
student_1 = Student(StudentID=1, FirstName="Pradip", LastName="Bochare", DateOfBirth=datetime(2002, 8, 3), Email="pradip@email.com", PhoneNumber="1234567890")
student_2 = Student(StudentID=2, FirstName="Abhishek", LastName="zune", DateOfBirth=datetime(2001, 2, 2), Email="abhishek@email.com", PhoneNumber="9876543210")

python_course = Course(101, "Python", "202", "Anjali")
student_1.EnrollInCourse(python_course)
student_2.EnrollInCourse(python_course)

enrollments = python_course.GetEnrollments()

print("Student Enrollments:")
for enrollment in enrollments:
    print(f"- Student ID: {enrollment.StudentID}, Student Name: {enrollment.FirstName} {enrollment.LastName}")
    """

    def GetTeacher(self):
        return self._assigned_teacher

    '''
python_teacher = Teacher(1,"Anjali", "Bhalchandra","bhalchandra@gmail.com")

python_course = Course(101, "Python",202,"Anjali")

python_course.AssignTeacher(python_teacher)

assigned_teacher = python_course.GetTeacher()
    '''

    @property
    def Enrollments(self):
        return self._enrollments

    # TASK9
    def Add_Course(self, CourseID, CourseName, CourseCode, InstructorName):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO course ( course_id, course_name, course_code, instructor_name) VALUES (%s, %s, %s, %s)"
            values = (CourseID, CourseName, CourseCode, InstructorName)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Course DETAILS ADDED  successfully.")

        except Exception as e:
            print(f"Error adding course details: {e}")

        finally:
            self._db_connector.close_connection()

    def retrieve_Coursecode(self, CourseCode):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM course where course_code=%s"
            values = (CourseCode,)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                course_details = cursor.fetchone()
            if course_details:
                print("Course Details:")
                print(f"Course ID:{course_details[0]}")
                print(f"Course Name:{course_details[1]}")
                print(f"Course Code: {course_details[2]}")
                print(f"Instructor Name: {course_details[3]}")
            else:
                print("coursecode not found.")
            self._db_connector.connection.commit()
        except Exception as e:
            print(f"Error getting course details: {e}")
        finally:
            self._db_connector.close_connection()

    def update_Course_instructorname(self, InstructorName, CourseID):
        try:
            self._db_connector.open_connection()

            query = "UPDATE Course SET instructor_name=%s where course_id=%s"
            values = (InstructorName, CourseID)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Course instructor UPDATED successfully.")

        except Exception as e:
            print(f"Error updating course details: {e}")

        finally:
            self._db_connector.close_connection()