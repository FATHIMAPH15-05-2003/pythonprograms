f=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\frame_works.txt","a")

frame_works=["python","java","spring"]

for fw in frame_works:
    f.write(fw+"\n")
f.close()
