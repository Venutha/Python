#Print if a number is odd or even . Take input from user 

n=input("Please enter the number")
if not n.isnumeric() :
  for count in range(0,3):
   n = input("Please enter a valid number")
   count+1
   if (n.isnumeric()):
     if(int(n)%2==0):
      print(f"number{n} is even ")
     else:
      print(f"number{n} is odd ")
     break
   



