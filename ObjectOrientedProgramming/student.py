class student:
    id:int
    name:str
    course:str

    def set_student(self,id,name,course):
        self.id=id
        self.name=name
        self.course=course

    def display_student(self):
        print(self.name,self.id,self.course)


student_instance1=student()

student_instance1.set_student(1,"fatima","djngo")
student_instance1.display_student()

