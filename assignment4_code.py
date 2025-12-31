#Assignment4 
#Exception Handling
#Write a Python program to handle a ZeroDivisionError.
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

#Write a program that accepts user input and handles a ValueError if the input is not an integer.
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: That was not a valid integer.")

#Write a program to open a file and handle a FileNotFoundError.
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError:
    print("Error: The file  not exist.")

#Write a Python program that uses try, except, else, and finally blocks.
try:
    num = int(input("Enter a number to divide 100 by: "))
    result = 100 / num
except Exception as e:
    print(f"An error occurred: {e}")
else:
    print(f"Success! The result is {result}")
finally:
    print("Execution complete.")

#Write a program to handle multiple exceptions in a single try block.
try:
    #  ValueError or ZeroDivisionError
    data = int(input("Enter a divisor: "))
    res = 10 / data
except (ValueError, ZeroDivisionError) as e:
    print(f"Caught a specific error: {e}")

#Text Files 
#Write a Python program to create a text file and write multiple lines into it.
lines = ["kavi\n", "keerthana\n", "kavikumar\n"]
with open("kee.txt", "w") as f:
    f.writelines(lines)

#Write a program to read the contents of a text file line by line.
with open("kee.txt", "r") as f:
    for line in f:
        print(line.strip())

#Write a Python program to count the number of lines, words, and characters in a text file.
line_count = 0
word_count = 0
char_count = 0
with open("kee.txt", "r") as f:
    for line in f:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)
print(f"Lines: {line_count}, Words: {word_count}, Characters: {char_count}")

#Write a program to copy the contents of one text file into another file.
with open("kee.txt", "r") as src:
    with open("keer.txt", "w") as dest:
        dest.write(src.read())

#Write a Python program to search for a specific word in a text file and display the line numbers where it appears.
search_word = "2"
with open("kee.txt", "r") as f:
    for line_num, line in enumerate(f, 1):
        if search_word in line:
            print(f"Found '{search_word}' on line {line_num}")
        else:
            print("not found word")


