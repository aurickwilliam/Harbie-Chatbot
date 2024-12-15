import mysql.connector

class Student_Record:
    def __init__(self):
        self.mydb = mysql.connector.connect(
          host="localhost",
          user="root",
          password="YuR1o_[rosie407]",
          database="harbie_school",
          autocommit=True
        )

    
    def check_student(self, std_info: dict) -> bool:
        cursor = self.mydb.cursor()
        query = f"SELECT student_no FROM students WHERE student_no = {std_info["std_no"]} AND first_name = '{std_info["fname"]}' AND last_name = '{std_info["lname"]}';"
        cursor.execute(query)

        return cursor.fetchall()
    

    def check_std_no_exists(self, number) -> bool:
        cursor = self.mydb.cursor()
        query = f"SELECT student_no FROM students WHERE student_no = {number}"
        cursor.execute(query)

        return cursor.fetchall()
    
    def get_student_info(self, std_no: int) -> tuple:
        cursor = self.mydb.cursor()
        query = f"SELECT * FROM students WHERE student_no = {std_no};"

        cursor.execute(query)

        return cursor.fetchone()


    def insert_student(self, student_info: dict):
        cursor = self.mydb.cursor()
        query = "INSERT INTO students (student_no, first_name, last_name, age, level, program, no_present, no_absent, total_balance, monthly_balance, gwa) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (
            student_info["student_no"],
            student_info["fname"],
            student_info["lname"],
            student_info["age"],
            student_info["level"],
            student_info["program"],
            0,
            0,
            0,
            0,
            0.0,
        )

        cursor.execute(query, values)
        self.mydb.commit()