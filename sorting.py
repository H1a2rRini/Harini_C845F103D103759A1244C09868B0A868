class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def get_student_details():
  name = input("Enter student's name: ")
  roll_number = input("Enter student's roll number: ")
  cgpa = float(input("Enter student's CGPA: "))
  return Student(name, roll_number, cgpa)


def sort_students(student_list):
  sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
  return sorted_students

num_students = int(input("Enter the number of students: "))
students = []
for i in range(num_students):
  print(f"Enter details for student {i + 1}:")
  student = get_student_details()
  students.append(student)
  
sorted_students = sort_students(students)

print("\nSorted list of students by CGPA:")
for student in sorted_students:
  print(
      f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}"
  )
