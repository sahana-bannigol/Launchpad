#Program4
list4=list3=list()
list3=eval(input("Enter the list elements"))
for i in range(len(list3)):
  x=0
  key=list3[i]
  for j in range(i):
   if(list3[i]==list3[j]):
     x=1
  if x==1:
   continue
  else:
      list4.append(list3[i])  
print(list4)