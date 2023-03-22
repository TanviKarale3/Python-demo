myFunc = lambda x, y: x * y  

print(myFunc(2, 3))                       #output: 6

#Here we are directly creating the function and passing the arguments
print((lambda x, y: x * y)(2, 3))         #same output i.e 6

print(type(lambda x, y: x * y))           #Output: <class 'function'>

# example to find squares of all numbers of a list
myList = [i for i in range(10)]

# returns square of each number
myFunc2 = lambda x: x * x

squares = list(map(myFunc2, myList))
print(squares)                              # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(list(map(lambda x: x * x, myList)))   #same as above
