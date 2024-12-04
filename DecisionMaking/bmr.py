weight=int(input("enter weight in kg:"))
height=int(input("enter height in cm:"))
age=int(input("enter age:"))
gender=(input("enter gender:")).lower()
print(weight,height,age,gender)
"""
(bmr)=
(10*weight[kg])+(6.25*height[cm]-(5*age[yrs])+5 for (male)
(10*weight[kg])+(6.25*height[cm]-(5*age[yrs])-161 for (female)
"""
if gender=="male":
    bmr=10*height+6.25*height-5*age+5
elif gender=="female":
    bmr=10*height+6.25-5*age-161
else:    
    print("***please enter a valid gender***")

print(bmr)    

activity_level=int(input("""
select activity level
press 1 for sedentary
press 2 for lightly active
press 3 for moderatly active
press 4 for very active
press 5 for extra active
"""))


if activity_level==1:
    calorie=bmr*1.2
elif activity_level==2:
    calorie=bmr*1.375
elif activity_level==3:   
    calorie=bmr*1.55
elif activity_level==4:
    calorie=bmr*1.725
elif activity_level==5:
    calorie=bmr*1.9
else:
    print(f"select a valid choice of activity")
print(f"total number of calorie in order to maintain your current weight={calorie}")    

target_weight=int(input("enter weight to increase in kg"))
duration=int(input("enter duration in weeks"))

# 1kg=7700
calorie_intake=target_weight*7700
days=duration*7
daily_calorie_intake=calorie_intake/days
print("daily_calorie_intake",daily_calorie_intake)

