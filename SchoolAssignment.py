class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

class School:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, grade):
        student = Student(student_id, name, grade)
        self.students.append(student)

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_students(self):
        for student in self.students:
            print(f"Student ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")


school = School()

school.add_student(1011, "Priyanka", 10)
school.add_student(1012, "Vamshi", 11)
school.add_student(1013, "Pushpa", 9)
school.add_student(1014, "Rajashekar",7) 
school.add_student(1015, "Pravalika", 6)

print("All Students:")
school.display_students()

student = school.find_student(1)
if student:
    print(f"Found Student: Student ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
else:
    print("Student not found.")