# Review
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# def greet():
#     print("Hello world!")
#     print("My name is Rafael!")
#     print("I really like Python!")
# greet()

# Function that allows for input
# def greet_with_name(name):
#     print(f"Hello {name}!")
#     print(f"How do you do {name}?")
#     print(f"{name}, do you like Python?")
# greet_with_name("Tchaina")

# Functions with more than 1 input
# def greet_with(name,location):
#     print(f"Hello {name}!")
#     print(f"Are you from {location}?")
# greet_with("Tchaina","Brasil")

# Functions with Keyword arguments
def greet_whit_keywords(name, location, age):
    print(f"Hello {name}?")
    print(f"Are you from {location}?")
    print(f"Are you {age} years old?")
greet_whit_keywords(name="Tchaina",age="15", location="Colombia")