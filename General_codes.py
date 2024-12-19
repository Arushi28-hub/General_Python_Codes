#IMP Building block Prblm 
print("Fibonnaci")
def fib(n):
   a,b=0,1
   print(a)
   print(b)
   for i in range (2,n):
       c=a+b
       print(c)
       a=b
       b=c
      
n=int(input("Enter the number for fibb : "))
print(fib(n))
print("******************************************")
print("Factorial")
num = int(input("Enter no. : "))

# Initialize the factorial variable to 1
factorial = 1

# Calculate the factorial using a for loop
for i in range(1, num + 1):
    factorial *= i

# Output: The factorial of the number
print(f"The factorial of {num} is {factorial}")
print("******************************************")
print("Sum of n no.s")
a = int(input("Enter a no. : "))
sum = 0 
i=1
for i in range(1,a+1):
 sum=sum+i
 i=i+1
print (sum)
print("******************************************")
print("Swapping")
# Swapping using third variable 
a =10
b=20
c=0
c=a
a=b
b=c
print(a) 
print(b)
# Swapping using no third variable 
a =10
b=20
a=a+b
b=a-b
a=a-b
print(a) 
print(b)
#swapping by tuple packing ad unpacking
a =10
b=20
c=0
a,b=b,a
print(a) 
print(b)
print("***************************************************")
print(" Check Armstrong Number for 3 digit only ")
num = int(input("Enter a number: "))
sum = 0
# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")
   
   
# Check Armstrong number of n digits
num = 1634

# Changed num variable to string, 
# and calculated the length (number of digits)
order = len(str(num))

# initialize sum
sum = 0

# find the sum of the cube of each digit
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

# Conversion of decimal number to binary number using base conversion Algo
def decimal_to_binary(decimal):
    # Initialize an empty string to store the binary result
    binary = ""
    
    # Perform the base conversion (divide by 2, keep track of remainders)
    while decimal > 0:
        remainder = decimal % 2  # Get remainder (0 or 1)
        binary = str(remainder) + binary  # Add the remainder to the left of the binary string
        decimal = decimal // 2  # Update the decimal number (integer division by 2)
    
    return binary if binary else "0"  # Return "0" for input 0

# Example usage:
decimal_number = int(input("Enter a decimal number: "))
print(f"The binary equivalent is: {decimal_to_binary(decimal_number)}")































