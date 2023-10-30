# KAGGLE - INTRODUCTION TO PROGRAMMING

#   Print Hello World Statement
print("Hello World")

#   Basic Addition
print(4+3)

#   Basic Subtraction
print(5-2)

# Parenthesis can control the order of operations.
print((1+3)*(9/2))

# Creating variables.
var1 = "My Name"
print(var1)

# Functions With Arguments
def add_three(input_variable):
    output_variable = (input_variable + 3)
    return output_variable

new_number = add_three(10)
print(new_number)

#   Functions With No Arguments
def happy_birthday():
    print("Hello User")
    print("Happy Birthday To You!!!")

happy_birthday()

# Data Types
# Integer
x = 14
print(type(x))

# Float
x = 14.66565651
print(type(x))

# Boolean
y = True
print(type(y))

# Strings
print(type(var1))
print(len(var1))

# Conditions
print( 3 > 2)

# IF Statements 
def evaluate_temp(temp):
    message = "Normal temperature."
    if temp > 38:
        message = "Fever!"
    return message

print(evaluate_temp(30))

# Multiple ELIF Statements
def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose

print(get_dose(17))

# Working With Lists
flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]

print(type(flowers_list))
print(flowers_list)

# The list has ten entries
print(len(flowers_list))

#   Indexing Lists
print("First entry:", flowers_list[0])









