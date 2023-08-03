class Principal:  
    def principal(self):  
        print("I'm Principal")  
class Teacher(Principal):  
    def teacher(self):  
        print("I'm Teacher")   
class Student(Teacher):  
    def student(self):  
        print("I'm student")  
d = Student()  
d.principal()  
d.teacher()  
d.student()