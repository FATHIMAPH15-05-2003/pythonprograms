class editor:
    name:str
    vendor:str

    def __init__(self,name,vendor):
        self.name=name
        self.vendor=vendor

    def display(self):
        print(self.name,self.vendor)

    def __str__(self):
        return self.name    


editor_instance1=editor("ramm","aritifical")
editor_instance1.display()     
print(editor_instance1)   