#ASSIGNMENT-3
#Map 
#Write a Python program using map() to convert a list of integers into their squares.
num = [1, 2, 3, 4]
s = list(map(lambda x: x**2, num))
print(s)

#Write a program using map() to convert all strings in a list to uppercase.
words = ["apple", "banana", "cherry"]
upper = list(map(str.upper, words))
print(upper)

#Given a list of temperatures in Celsius, use map() to convert them to Fahrenheit.
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

#Write a program using map() to calculate the length of each word in a list of strings.
words = ["Python", "Map", "Function"]
lengths = list(map(len, words))
print(lengths)

#Use map() to add 10 to each element of a given list of numbers.
nums = [5, 15, 25]
k = list(map(lambda x: x + 10, nums))
print(k)

#Filter 
#Write a Python program using filter() to extract all even numbers from a list.
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

#Write a program using filter() to select all words from a list that start with a vowel.
words = ["apple", "banana", "orange", "ice", "pear"]
vowels = list(filter(lambda w: w[0].lower() in 'aeiou', words))
print(vowels)

#Given a list of integers, use filter() to remove all negative numbers.
nums = [-10, 5, -2, 0, 8]
p= list(filter(lambda x: x >= 0, nums))
print(p)

#Write a program using filter() to find numbers greater than 50 from a list.
nums = [25, 60, 12, 100, 49]
a = list(filter(lambda x: x > 50, nums))
print(a)

#Use filter() to extract all palindromic strings from a list.
words = ["radar", "hello", "level", "world", "madam"]
pali = list(filter(lambda w: w == w[::-1], words))
print(pali)

