#Return the largest number among three using conditional statements

num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
num3=int(input("Enter the third number:"))

if num1>num2 and num1>num3:
  print(f"{num1} is greater than {num2} and {num3}")
elif num2>num1 and num2>num3:
    print(f"{num2} is greater than {num1} and {num3}")
elif num3>num1 and num3>num2:
    print(f"{num3} is greater than {num2} and {num1}")
else:
    print(f"{num1} and {num2} and {num3} are all equal")


#Voting system
numAge=int(input("Enter your age:"))

if numAge>18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")