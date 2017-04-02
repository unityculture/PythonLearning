print('hi' + ' there !')
print("hi", "there")
print(str(5) + 'hi')
# print(5 + 'hi') -> cannot convert
print(int('5') + 5)
# print(int('5.5') + 5) -> 5.5 is not integer
print(int('5') + 5)

# Math
print(5 / 34)
print(2**3)

# Variables
exampleVar = 55 + 32
print(exampleVar)
exampleVar = print(55 + 32)

x, y = (3, 5)
print(x)
print(y)
# Length need to be equal !
## x, y = (3, 5, 1)
# print(x)
# print(y)

# While Loop
condition = 1
while condition < 10:
    print(condition)
    condition += 1
    # condiction = condiction + 1

# while True:
#     print('doing stuff')

# For Loop
exampleList = [1, 5, 3, 2]

for eachNumber in exampleList:
    print(eachNumber)
    print("I am python")

for x in range(1, 11):
    print(x)

help(type)
