#Program2
list1=list2=list()
list1=eval(input("Enter the list elements"))

for i in range(len(list1)):
  if list1[i]<5:
    list2.append(list1[i])
  else:
    continue
  i=i+1
print(list2)