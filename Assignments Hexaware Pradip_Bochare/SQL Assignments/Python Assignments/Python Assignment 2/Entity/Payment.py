#from Student import Student
from datetime import datetime

class Payment:
    def __init__(self, PaymentID, StudentID, Amount, PaymentDate):
        self._PaymentID = PaymentID
        self._StudentID = StudentID
        self._Amount = Amount
        self._PaymentDate = PaymentDate
    def __init__(self, db_connector):
        self._db_connector = db_connector
    @property
    def PaymentID(self):
        return self._PaymentID

    @PaymentID.setter
    def PaymentID(self, new_PaymentID):
        if isinstance(new_PaymentID, int) and new_PaymentID > 0:
            self._PaymentID = new_PaymentID
        else:
            raise ValueError("Payment ID must be a positive integer.")

    @property
    def StudentID(self):
        return self._Student

    @StudentID.setter
    def StudentID(self, new_Student):
        if isinstance(new_Student,int):
            self._Student = new_Student
        else:
            raise ValueError("Invalid Student reference.")

    @property
    def Amount(self):
        return self._Amount

    @Amount.setter
    def Amount(self, new_Amount):
        if isinstance(new_Amount, (int, float)) and new_Amount >= 0:
            self._Amount = new_Amount
        else:
            raise ValueError("Amount must be a non-negative number.")

    @property
    def PaymentDate(self):
        return self._PaymentDate

    @PaymentDate.setter
    def PaymentDate(self, new_PaymentDate):
        if isinstance(new_PaymentDate, str) and len(new_PaymentDate) == 10:
            self._PaymentDate = new_PaymentDate
        else:
            raise ValueError("Invalid payment date format.")

    def GetStudent(self):
       pass

    def GetPaymentAmount(self):
        return self.Amount

    def GetPaymentDate(self):
        return self.PaymentDate

    '''
payment = Payment(101, 1, Amount=50, PaymentDate="2023-12-12")

# Retrieve payment amount and date
payment_amount = payment.GetPaymentAmount()
payment_date = payment.GetPaymentDate()

# Display payment information
print(f"Payment Amount: {payment_amount}")
print(f"Payment Date: {payment_date}")
    '''

    # TASK 10
    def Add_Payment(self, PaymentID, StudentID, Amount, PaymentDate):
        try:
            self._db_connector.open_connection()

            query = "INSERT INTO payments (payment_id, student_id, amount,payment_date) VALUES (%s, %s, %s, %s)"
            values = (PaymentID, StudentID, Amount, PaymentDate)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Payment DETAILS ADDED  successfully.")

        except Exception as e:
            print(f"Error adding payment details: {e}")

        finally:
            self._db_connector.close_connection()

    def retrieve_studentrecord(self, StudentID):
        try:
            self._db_connector.open_connection()

            query = "SELECT * FROM students where student_id=%s"
            values = (StudentID,)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)
                student_details = cursor.fetchone()
            if student_details:
                print("student_details:")
                print(f"Student ID:{student_details[0]}")
                print(f"Student First Name:{student_details[1]}")
                print(f"Student Last Name:{student_details[2]}")
                print(f"Date Of Birth: {student_details[3]}")
                print(f"Email: {student_details[4]}")
                print(f"Phone no:{student_details[5]}")
            else:
                print("student id not found.")
            self._db_connector.connection.commit()
        except Exception as e:
            print(f"Error getting course details: {e}")
        finally:
            self._db_connector.close_connection()

    def update_payment_amount(self, Amount, StudentID):
        try:
            self._db_connector.open_connection()

            query = "UPDATE Payments SET Amount=%s where student_id=%s"
            values = (Amount, StudentID)

            with self._db_connector.connection.cursor() as cursor:
                cursor.execute(query, values)

            self._db_connector.connection.commit()
            print("Student balance  UPDATED successfully.")

        except Exception as e:
            print(f"Error updating student balance details: {e}")

        finally:
            self._db_connector.close_connection()
