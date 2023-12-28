#from Entity.Course import Course
class Teacher:
    def __init__(self, TeacherID, FirstName, LastName, Email):
        self._TeacherID = TeacherID
        self._FirstName = FirstName
        self._LastName = LastName
        self._Email = Email
        self.AssignedCourses = []

    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def TeacherID(self):
        return self._TeacherID

    @TeacherID.setter
    def TeacherID(self, new_TeacherID):
        if isinstance(new_TeacherID, int) and new_TeacherID > 0:
            self._TeacherID = new_TeacherID
        else:
            raise ValueError("Teacher ID must be a positive integer.")

    @property
    def FirstName(self):
        return self._FirstName

    @FirstName.setter
    def FirstName(self, new_FirstName):
        if isinstance(new_FirstName, str) and new_FirstName:
            self._FirstName = new_FirstName
        else:
            raise ValueError("First name must be a non-empty string.")

    @property
    def LastName(self):
        return self._LastName

    @LastName.setter
    def LastName(self, new_LastName):
        if isinstance(new_LastName, str) and new_LastName:
            self._LastName = new_LastName
        else:
            raise ValueError("Last name must be a non-empty string.")

    @property
    def Email(self):
        return self._Email

    @Email.setter
    def Email(self, new_Email):
        if isinstance(new_Email, str) and "@" in new_Email:
            self._Email = new_Email
        else:
            raise ValueError("Invalid email format.")

    def UpdateTeacherInfo(self, teacherID, firstName, lastName, email):
        self.TeacherID = teacherID
        self.FirstName = firstName
        self.LastName = lastName
        self.Email = email
        print("Teacher information updated successfully.")

    '''   
teacher_info = Teacher(1, "Professor","Johnson","prof.johnson@example.com") 
teacher_info.UpdateTeacherInfo(101,"ms Anjali","Bhalchandra","bhalchandra@gmail.com")
     '''

    def DisplayTeacherInfo(self):
        print(f"Teacher ID: {self.TeacherID}")
        print(f"First Name Code: {self.FirstName}")
        print(f"Last Name: {self.LastName}")
        print(f"Email : {self.Email}")

    '''    
teacher = Teacher(1, "Professor","Johnson","prof.johnson@example.com")
teacher.DisplayTeacherInfo()
    '''

    # TASK 5
    def AssignToCourse(self, course):
        self.AssignedCourses.append(course)
        print(f"Teacher {self.FirstName} {self.LastName} assigned to {course.CourseName}.")

    '''
teacher = Teacher(1, "Professor", "Anjali", "prof.anjali@email.com")
python_course = Course(101, "Python", "101", "Professor Anjali")

teacher.AssignToCourse(python_course)
    '''

    # TASK 9
    def Add_Teacher(self, TeacherID, FirstName, LastName, Email):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO teacher ( teacher_id, first_name, last_name, email) VALUES (%s, %s, %s, %s)"
            values = (TeacherID, FirstName, LastName, Email)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Teacher DETAILS ADDED  successfully.")

        except Exception as e:
            print(f"Error adding student details: {e}")

        finally:
            self._db_connector.close_connection()