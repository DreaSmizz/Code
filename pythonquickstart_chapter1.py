# price = input("What is the price of a cup of coffee? ")
# cups = int(input("How many cups do you want? "))
# total = float(price) * int(cups)
# print(f"Your total is ${total} for {cups} cups.")
#
# first_name = input("Please enter your name: ")
# print(f"The first letter of your name is: {first_name[:1]}.")

# grades = {"A", "B", "C", "D", "F"}
# for grade in grades:
#     print(grade)

temps = [
    [
    [66, 34],
    [57, 25],
    [49, 45],
    [45, 19],
    [33, 7],
    [32, 14],
    [49, 37]
],
    [
    [52, 39],
    [61, 51],
    [64, 51],
    [67, 57],
    [69, 42],
    [32, 14],
    [49, 37],
        ]
]

# Day 1 temps
# Print first set of temps
#print(temps[0])
# Print only the first temperature in the first set
# print(temps[0][0])
# print(temps[1][2][1])
#
# a = 1
# b = 2
# c = 3
#
# if a > b:
#     print("a is greater than b")
#     if b != c:
#         print("but b is not equal to c")
#     else:
#         print("b is equal to c")
# else:
#     print("a is less than b")

singular_words = ['student', 'teacher', 'room']
for word in singular_words:
    print(word + 's')
else:
    print("Done!")

# The planets
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Display the planet and its number
for index, value in enumerate(planets):
    print("Planet " + str(index) + ": " + value)

for index, value in enumerate(planets):
    print("Planet " + str(index + 1) + ": " + value)
