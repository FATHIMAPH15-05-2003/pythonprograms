class cusine:
    cusine_name:str

    def __init__(self,cusine_name):
        self.cusine_name=cusine_name

    def display(self):
        print(self.cusine_name)


class Mealtype:

    name=str

    def __init__(self,name):
        self.name=name
    def dispaly(self):
        print(self.name)


class Dish(Mealtype,cusine):
    dish_name:str

    def __init__(self,dish_name):
        self.dish_name=dish_name

    def display(self):
        print(self.dish_name)

dish_instance=Dish()
dish_instance.display("indian","breakfast","gheeroast") 
print(dish_instance)       


                