#Python if statement

number = 10

# check if number is greater than 0
if number > 0:
    print('Number is positive.')

print('The if statement is easy')


#Python If else statement

number = 10

if number > 0:
    print('Positive number')

else:
    print('Negative number')

print('This statement is always executed')


#python if...elif..else statement

number = 0

if number > 0:
    print("Positive number")

elif number == 0:
    print('Zero')
else:
    print('Negative number')

print('This statement is always executed')


#Python Nested If statement

number = 5

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')


#Python Ternary operator

# Program to demonstrate conditional operator
a, b = 10, 20
 
# Copy value of a in min if a < b else copy b
min = a if a < b else b
 
print(min)