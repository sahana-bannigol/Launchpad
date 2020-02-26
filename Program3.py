#Program3
list4=list3=list()
list3=eval(input("Enter the list elements"))
key=int(input("Enter Search element"))
for i in range(len(list3)):
  if(list3[i]==key):
    list4.append(i)
  i=i+1
print(list4)