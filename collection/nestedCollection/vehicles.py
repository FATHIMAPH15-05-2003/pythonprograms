cars=[
    {"id":1,"name":"fronx","price":1200000,"brand":"nexa","colors":["red","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":2,"name":"baleno","price":1100000,"brand":"nexa","colors":["grey","blue","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":3,"name":"3xo","price":900000,"brand":"mahindra","colors":["red","white","black"],"transmissions":["amt","cvt"]},
    {"id":4,"name":"punch","price":700000,"brand":"tata","colors":["red","blue","white","green"],"transmissions":["manuel","cvt"]},
    {"id":5,"name":"nexon","price":1400000,"brand":"tata","colors":["red","white"],"transmissions":["manuel","amt","cvt"]},
    {"id":6,"name":"kiger","price":1000000,"brand":"renault","colors":["blue","white"],"transmissions":["manuel","cvt"]},
    {"id":7,"name":"taigun","price":2300000,"brand":"volkswagon","colors":["red","blue","white"],"transmissions":["manuel","cvt"]},
]
#count
print(len(cars))

#print available color of baleno
for c in cars:
    if c.get("name")=="baleno":
        print(c.get("colors"))

        # or
baleno_colors=[c.get("colors")for c in cars if c.get("name")=="baleno"] 
print(baleno_colors)       

#print all brands 

all_brands=[c.get("brands") for c in cars]
print(all_brands)

#print amt in transmission

amt_cars=[c.get("name") for c in cars if "amt" in c.get("transmissions")]
print(amt_cars)

#print blue color casr

blue_cars=[c.get("name")for c in cars if "blue" in c.get("colors")]
print(blue_cars)

#print all transmission

transmission_types={t for c in cars for t in c.get("transmissions")}
print(transmission_types)


#print all color

all_colors={cl for c in cars for cl in c.get("colors")}
print(all_colors)


