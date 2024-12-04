f1=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\all_students.txt")
f2=open("C:\\Users\\fathi\\OneDrive\\Desktop\\python\\datasets\\failed.txt")

all_student=set()
failed=set()

for line in f1:
    line=line.rstrip("\n")
    all_student.add(line)

for line in f2:
    line=line.rstrip("\n")
    failed.add("\n")

passed_student=all_student.difference(failed) 
print(passed_student)  
f1.close()
f2.close() 