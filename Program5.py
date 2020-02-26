#Program5
string2=" "
string=input("Enter a sentence")
list1=string.split()
for i in range(len(list1)):
  string2=string2+list1.pop()+" "
print(string2)