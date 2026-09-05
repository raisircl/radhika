num=int(input("enter a number "))
sum=0
rev=0
while num>0: # 513, 51
    sum+=num%10 # 0+3 => 3, 3+1 => 4, 4+5 => 9
    rev=(rev*10)+(num%10) # 0*10+513%10 => 3, 3*10+51%10 => 31, 31*10+5%10 => 315
    num//=10 # 513//10 => 51, 51//10 => 5, 5//10 => 0

print(f"Sum of digits: {sum}")
print(f"Reversed number: {rev}")

