class students:
    def __init__(self, name, grade, rollno, section):
        self.name = name
        self.grade = grade
        self.rollno = rollno
        self.section = section

class StudentManagement(students):
    def __init__(self):
        self.students = []


    def display(self):
        if len(self.students) == 0:
            print("Empty array")
        else:
            for i in self.students:
                print(i)
        
    def accept(self):
        try:
            name = input("Enter the name ")
            Grade = int(input("Enter the Grade "))
            Section = input("Enter the section")
            rollno = int(input("Enter the rollno"))
            c = {"name": name,"grade":Grade,"section":Section,"rollno":rollno}
            self.students.append(c)
            return c
        except ValueError:
            print("Invalid Value input. Please enter a valid value")
        
    def delete(self):
        try:
            rollno = int(input("Enter the rollno to be deleted"))
            removed = False
            for students in self.students:
                if students["rollno"] == rollno:
                    self.students.remove(students)

                    removed = True
                    return
            if removed == True:
                print("Student Deleted")
            else:
                print("Student not found")
        except ValueError:
            print("Invalid rollno")

    def update(self):
        try:
            rollno = int(input("Enter the rollno to update the details"))
            for students in self.students:
                if students["rollno"] == rollno:
                    name = input("The name of the student")
                    grade = int(input("The Grade of student"))
                    section = input("The section of the student")
                    self.students.remove(students)
                    b = {"name":name ,"grade":grade ,"section":section ,"rollno":rollno}
                    self.students.append(b)

                else:
                    print("Student not found")
        except ValueError:
            print("Invalid rollno")
    def search(self):
        try:
            x = int(input("Enter the rollno of student to display his details: "))
            for students in self.students:
                if students["rollno"] == x:
                    print(students) 
                else:
                    print("Student not found")
        except ValueError:
            print("rollno not valid")
def main():
    
    sm = StudentManagement()

    while True:
        print("Student Management System")
        print("---------------------------")
        print("1. Accept")
        print("2. Display")
        print("3. Delete")
        print("4. Update")
        print("5. Search")
        print("0. Exit")

        ch = int(input("Enter your choice: "))
        if ch == 0:
            print("Thank you")
            break;
        elif ch ==1:
            sm.accept()
        elif ch == 2:
            sm.display()
        elif ch == 3:
            sm.delete()
        elif ch == 4:
            sm.update()
        elif ch == 5:
            sm.search()
        else:
            print("Wrong choice entered")

main()