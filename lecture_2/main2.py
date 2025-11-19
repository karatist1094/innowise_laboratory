def generate_profile(age):
    """Determines life stage according to the age"""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Unknown"

# Greeting
print("Hello! Please enter a little information about yourself")

# Getting information
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your year of birth: ")

# Transformation and calculations
birth_year = int(birth_year_str)
current_age = 2025 - birth_year

# Getting hobbies
hobbies = []

while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish: ")
    if hobby.lower() == "stop":
        break
    hobbies.append(hobby)

# Profile generation
life_stage = generate_profile(current_age)

# Creating dictionary
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

# Output
print("PROFILE:")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']} years old")
print(f"Life stage: {user_profile['stage']}")

# Hobby processing
if not user_profile['hobbies']:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
    for hobby in user_profile['hobbies']:
        print(f"- {hobby}")
