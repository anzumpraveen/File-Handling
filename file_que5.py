a=["anzum","dhano","khushboo","kajal"]
f=open("student-list.txt","w")
for i in range(0,len(a)):
    f.write(a[i])
    f.write("\n")
f=open("student-list.txt","r")
print(f.read())
f.close()


