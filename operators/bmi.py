#Bmi=weight_in_kg/(height_in_meter)**2

weight_in_kg=int(input("enter weight in kg:"))
height_in_cm=int(input("enter height in cm:"))
height_in_meter=height_in_cm/100
Bmi=weight_in_kg/height_in_meter**2
Bmi=round(Bmi,2)
print(Bmi)

#print under weight if bmi <19
#print normal weight if bmi 19 to <25
#print overweight if bmi 25 to <30
#print obese if bmi >=30

if Bmi<19:
   print("under weight")
elif Bmi<25:
   print("normal weight")
elif Bmi<30:
   print("over weight")
elif Bmi>=30:
   print("obese")#Bmi=weight_in_kg/(height_in_meter)**2



