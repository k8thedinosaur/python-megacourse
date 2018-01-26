# Create a function that converts Celsius degrees to Fahrenheit.
# The formula to convert Celsius to Fahrenheit is F = C × 9/5 + 32.


# def celsius_to_fahrenheit(c):
#     if c < -273.15:
#         print("Absolute zero reached. Terminating Earth.")
#     else:
#         f = c * 9 / 5 + 32
#         print("{} Degrees F".format(f))
#
#
# temperatures = [10, -20, -289, 100]
#
# for c in temperatures:
#     celsius_to_fahrenheit(c)

# print("{} Degrees F".format(f))


# print("{} Degrees F".format(f))


# Create a function that takes any string as argument and returns the length of that string.


# def string_length(mystring):
#     if type(mystring) == int:
#         print("Impossible to calculate string length of integer.")
#     elif type(mystring) == float:
#         print("Impossible to calculate string length of float.")
#     else:
#         return len(mystring)
#
#
# mystring = input("Enter a string: ")
# string_length(mystring)
# print("Your string is {} characters long.".format(string_length(mystring)))


# Create a for  loop block that iterates through the following list and prints out each item of the list in each iteration.
#
# mylist = [1, 2, 3, 4, 5]
#
# for i in mylist:
#     if i > 2:
#         print(i)

# file = ("example.txt",'w')
# numbers = [1, 2, 3]
# for i in numbers:
#     file.write(str(i)+'\n')
#
# file.close()

temperatures = [10, -20, -289, 100]


def writer(temperatures):
    with open("temps.txt", 'w') as file:
        for c in temperatures:
            if c > -273.15:
                f = c * 9 / 5 + 32
                file.write(str(f) + "\n")


writer(temperatures)  # Here we're calling the function, otherwise no output will be generated