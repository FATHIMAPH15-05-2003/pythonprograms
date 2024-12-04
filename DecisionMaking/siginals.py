#syntax
#if condition:
    #state1
#elif condition:
    #state2
#elif condition:
    #state3
#else:
    # default state

siginal=int(input("enter siginal:"))

if siginal=="Red":

    print("STOP")

elif siginal=="Green":

    print("GO")

elif siginal=="Yellow":

    print("WAIT")   

else:

    print("invalid siginal")                         

