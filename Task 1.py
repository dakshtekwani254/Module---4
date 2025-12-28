#Task 1: Calculate Factorial Using a Function 

def factorial(n):
    if n==1:
        return 1
    else:
        fact= n * factorial(n-1)
    
    return fact
    
print("Calculating Factorial\n")
number=int(input("Enter number: "))
print(f"Factorial of {number} is: {factorial(number)}")

#Sample Output
'''
Calculating Factorial

Enter number: 5
Factorial of 5 is: 120
'''
