class Classroom:
    def __init__(self):
        self.students = [] 

    def add_student(self, name):
        self.students.append(name)

    def count_students(self):
        return len(self.students)



room = Classroom()
room.add_student("Ali")
room.add_student("Sara")

print(room.count_students())  