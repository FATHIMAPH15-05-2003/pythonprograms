class person:
    name:str
    age:int

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def display_person_info(self):
        print(self.name,self.age)


class Employee:
    emp_id:int
    salary:int

    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def displayemployee_info(self):
        print(self.emp_id,self.salary)


class Manager(Employee,person):
    department:str

    def __init__(self,age,name,emp_id,salary,department):

        Employee.__init__(self,emp_id,salary)
        person.__init__(self,name,age)
        self.department=department


    def display_manager_info(self):

        self.displayemployee_info()
        self.display_person_info()

        print(self.department)

manager_instance=Manager("e01",5400,"manu",34,"science") 
manager_instance.display_manager_info()   
print(manager_instance)    
