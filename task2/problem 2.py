x = int (input("enter the number: "))
y=0
for i in range (x+1) :
    if i>0:
        if i%2==0:
            y+=i
print ("The sum of even numbers from 1 to " , x , "is" , y)