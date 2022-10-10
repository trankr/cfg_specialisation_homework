"""

TASK 2

Write a base class to represent a student. Below is a starter code.
Feel free to add any more new features to your class.
As a minimum a student has a name and age and a unique ID.

Create a new subclass from student to represent a concrete student doing a specialization, for example:
Software Student and Data Science student.

"""


class Student:

    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

    def add_subject(self, subject, grade = "N/A"):
        # Updating dictionary with subject and grade. If no grade is inputted, the grade is N/A instead.
        self.subjects.update({subject: grade})

    def remove_subject(self, subject):
        self.subjects.pop(subject)

    def view_subjects(self):
        print("Subjects taken: " + str(list(self.subjects.keys())))

    def view_subject_details(self):
        print("Subjects and grades: " + str(self.subjects))

    def get_average(self):
        # Check if the inputted grades are numbers.
        # Add the (numbered) grades up and divide it by the number of (numbered) grades to return an average.

        all_grades = list(self.subjects.values())
        no_grades = 0
        total_grade = 0

        for grade in all_grades:
            if type(grade) == int or type(grade) == float:
                no_grades +=1
                total_grade += grade

        average_grade = total_grade/no_grades

        return average_grade

    def view_average(self):
        print("Average grade: " + str(self.get_average()))

    def view_student_details(self):
        print("Name: " + str(self.name))
        print("Age: " + str(self.age))
        print("id: " + str(self.id))


class CFGStudent(Student):

    def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation
#     create new methods that manage student's subects (add/remove new subject and its graade to the dict)
#     create a method to view all subjects taken by a student
#     create a method  (and a new variable) to get student's overall mark (use average)

    def view_student_details(self):
        # Adding specialisation detail for CFG students.
        super(CFGStudent, self).view_student_details()
        print("Specialisation: " + str(self.specialisation))

# EXAMPLE code run:
# Creating student Kristine - adding subjects, one without a grade.
print("Example student")
kristine = CFGStudent("Kristine", 22, 2109, "Software")
kristine.view_student_details()
kristine.add_subject("Law", 71)
kristine.add_subject("Foundation", 60)
kristine.add_subject("Specialisation")

# Checking all subject details inputted correctly.
kristine.view_subject_details()

# Checking average calcuation.
print("\nExample grade average")
kristine.view_average()

# Removing a subject.
print("\nExample subject removal")
kristine.remove_subject("Foundation")
kristine.view_subjects()

# Adding a grade where it was not inputted prior.
print("\nExample grade addition§")
kristine.add_subject("Specialisation", 87)
kristine.view_subject_details()
