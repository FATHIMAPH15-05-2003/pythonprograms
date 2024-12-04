class Superhero:
    name:str
    suit:str

    def __init__(self,name,suit):
        self.name=name
        self.suit=suit
    def __str__(self):
        return self.name
    
class Spiderman(Superhero):
    def __init__(self,name,suit):

            super().__init__(name,suit)

    def super_power(self):
            print("spidrman","web shooting","sticky hands")

spider_instance=Spiderman("spiderman","spidermansuit")
print(spider_instance)
spider_instance.super_power()  


class minnalmurali(Superhero):
     def __init__(self,name,suit):
          
          super().__init__(name,suit)

     def super_power(self):
          print("minnalmurali","jumbing","action") 

minnalmurali_instance=minnalmurali("minnalmurali","minnalmuralisuit")
print(minnalmurali_instance)
minnalmurali_instance.super_power()          
