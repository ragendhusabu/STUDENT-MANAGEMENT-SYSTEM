
from mysql import connector
import datetime


class DbStudent:

    def get_connected(self):
        try:
            self.connection = connector.connect(
                host="localhost",
                user="root",
                password="321996",
                database="student_db"
            )
            return self.connection

        except Exception as e:
            return None


class StudentManager(DbStudent):

    def get_object(self, id=None):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()

            query = "select * from student where id=%s"
            values = (id,)

            self.cursor.execute(query, values)
            students = self.cursor.fetchone()

            return students

        except Exception as e:
            return None

    def post(self, **kwargs):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()

            query = """
            insert into student
            (student_name, department, course, email, phone, fees, joining_date)
            values(%s,%s,%s,%s,%s,%s,%s)
            """

            values = [v for v in kwargs.values()]

            self.cursor.execute(query, values)
            self.connection.commit()

            print("Student Added Successfully...!")

        except Exception as e:
            print(e)

    def get(self):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()

            query = "select * from student"

            self.cursor.execute(query)
            students = self.cursor.fetchall()

            for i in students:
                print(i)

        except Exception as e:
            print(e)

    def put(self, id=None, **kwargs):
        try:
            students = self.get_object(id=id)

            if students != None:

                self.connection = super().get_connected()
                self.cursor = self.connection.cursor()

                placeholder = ""

                for k in kwargs.keys():
                    placeholder += k + "=%s,"

                placeholder = placeholder.rstrip(", ")

                query = f"update student set {placeholder} where id=%s"

                values = [v for v in kwargs.values()]
                values.append(id)

                self.cursor.execute(query, values)
                self.connection.commit()

                print("Student Data Updated Successfully...")

            else:
                print("Student Not Found..!")

        except Exception as e:
            print(e)

    def delete(self, id=None):
        try:
            self.connection = super().get_connected()
            self.cursor = self.connection.cursor()

            query = "delete from student where id=%s"
            values = (id,)

            self.cursor.execute(query, values)
            self.connection.commit()

            print('deleted success')

            if self.cursor.rowcount > 0:
                print("Deletion successful")
            else:
                print("Student not found")

        except Exception as e:
            print(e)


student_instance = DbStudent()
student_instance.get_connected()

student_instance = StudentManager()

#print(student_instance.get_object(1))


# POST

#student_instance.post(student_name="Rahul",department="Computer Science",course="Python Full Stack",email="rahul@gmail.com",phone="9876543210",fees=25000,joining_date=datetime.date.today())

#student_instance.post(student_name="Anjali",department="Electronics",course="Data Science",email="anjali@gmail.com",phone="9876543211",fees=30000,joining_date=datetime.date.today())

#student_instance.post(student_name="Arjun",department="Computer Science",course="Python Programming",email="arjun@gmail.com",phone="9876543212",fees=18000,joining_date=datetime.date.today())


# GET
student_instance.get()


# PUT
#student_instance.put(1, fees=28000)


# DELETE
#student_instance.delete(3)
