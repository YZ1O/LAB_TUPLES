numbers:int=(1,2,3)
letters:str=("a", "b", "c")
print(numbers[0],letters[-1])

result = numbers + letters
print(len(result))

if 4 in result:
    print("4 is in the tuple !")
else:
    print("4 is not in the tuple")

numberOflist = [4, 5, 6]
convertTuple=tuple(numberOflist)
print(convertTuple)
number1,number2,number3 = convertTuple
print(number1,number2,number3)