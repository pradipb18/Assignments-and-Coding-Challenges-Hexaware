
#from Entity.Course import Course
#from Entity.Enrollment import Enrollment
#from Entity.Payment import Payment
#from Entity.Student import Student
from Entity.Teacher import Teacher
from util.DatabaseConnector import DatabaseConnector


db_connector = DatabaseConnector(host ="localhost", database ="sisdb", user ="root", password ="pradip")
db_connector.open_connection()

#students_manager= Student(db_connector)

#students_manager.Add_Student(11,"John","Doe","1995-08-15","john.doe@example.com","1234567890")

#enrollments_manager =Enrollment(db_connector)

#enrollments_manager.Enroll_Course(109,11,201)
#enrollments_manager.Enroll_Course(110,11,202)
#enrollments_manager.retrieve_enrollment_record(202)
#enrollments_manager.retrieve_enrollment_record(212)

#course_manager =Course(db_connector)
#course_manager.Add_Course(211,"Advanced Database Management","CS302","Sarah Smith")
#course_manager.retrieve_Coursecode("CS302")
#course_manager.update_Course_instructorname("Prof karthika",211)



teacher_manager=Teacher(db_connector)
#teacher_manager.Add_Teacher(311,"Sarah", "Smith"," sarah.smith@example.com")


#payments_manager=Payment(db_connector)
#payments_manager.Add_Payment(411,11,500,"2023-04-10")
#payments_manager.retrieve_studentrecord(101)
#payments_manager.update_payment_amount(5000,101)

db_connector.close_connection()