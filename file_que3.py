banks_list = ["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
f=open("file-question3.txt","w")
for i in range(0,len(banks_list)):
    f.write(banks_list[i])
    f.write("\n")
f=open("file-question3.txt","r")
print(f.read())
f.close()



