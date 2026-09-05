num=int(input("enter a number"))
i=2
while i<num:
    if num%i==0:
        break
    i+=1
if i==num:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")