f=open("people1-exercise.txt","r")
g=open("delhi.txt","a")
h=open("shimla.txt","a")
x=open("other.txt","a")
a=f.read()
j=a.split("\n")
for i in range(0,len(j)):
    if "delhi" in j[i]:
        g.write(j[i])
        g.write("\n")
    elif"shimla" in j[i]:
        h.write(j[i])
        h.write("\n")
    else:
        x.write(j[i])
        x.write("\n")
f=open("people1-exercise.txt","r")
print("FULL LIST")
print(f.read())
f.close()
g=open("delhi.txt","r")
print("DELHI")
print(g.read())
g.close()
h=open("shimla.txt","r")
print("SHIMLA")
print(h.read())
h.close()
x=open("other.txt","r")
print("OTHER")
print(x.read())
h.close()





