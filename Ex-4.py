#List
from ast import Lambda


chars = list ("Hello World")
print(chars)

numbers= list(range(20))
print(numbers)

#Accessing items in a list
numbers= list(range(20))
print(numbers[::2])

#adding items to a list
letters = ["a", "b", "c"]
letters.append("d")
print(letters)

#removing a letter form the list
letter = ["a", "b", "c"]
letter.remove("b")
print(letter)

#finding items in list
letters = ["a", "b", "c"]
print(letters.index("c"))

#sorting number in descending order
numbers = [3, 51, 5, 82, 6, 30]
numbers.sort(reverse=True)
print(numbers)

#LMBDA Function
items = [("Product1", 10), ("Product2", 6), ("Product3", 5)]
items.sort(key=lambda item:item[1])
print(items)

#Filter Function
filtered = list(filter(lambda item:item[1]>=6, items))
print(filtered)