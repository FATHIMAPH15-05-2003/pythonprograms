class facutly:
    id:int
    name:str
    age:int
    course:str
    experience:int

    def set_facutly(self,id,name,age,course,experience):
        self.id=id
        self.name=name
        self.age=age
        self.course=course
        self.experience=experience

    def display_facutly(self):
        print(self.name,self.age,self.course,self.experience)

#object create......refrence_name=classname()
facutly_instance1=facutly()
facutly_instance2=facutly()
facutly_instance2.set_facutly(100,"sabir",27,"bigdata",4)
facutly_instance2.display_facutly()           
