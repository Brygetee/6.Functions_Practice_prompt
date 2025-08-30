"""
6. Functions
What you should know: Define and call reusable blocks of code with
parameters and return values.
Practice Prompt: Create a function calculate_fabric_needed(project_type)
that returns how many yards are required for "skirt", "dress", or "pillowcase".
"""
"""----------------------------Initial Code---------------------------------------"""
# def calculate_fabric_needed(project_type):
#     if project_type == "skirt":
#         yards = "2 yards"
#         return yards
#     elif project_type == "dress":
#         yards = "4 yards"
#         return yards
#     elif project_type == "pillowcase":
#         yards = "1 yard"
#         return yards
#     else:
#         print("Please type a valid response.")

# print(calculate_fabric_needed("pillowcase"))

"""----------------------------How to improve code----------------------
1. Ask the user for input instead of relying on them to call the function with their choice.
2. Instead of being redundant with defining yards and returning 
its better to use a dictionary lookup
3. It is better to use a while loop rather than recursion when dealing with user input.
---------notes---------------
.get(key, default) is a dictionary method that looks for a key.
If the key exists, it returns its value.
If the key doesn’t exist, it returns the default value you provide.

"""
def calculate_fabric_needed(project_type):
    fabric_requirements = {
        "skirt": "2 yards",
        "dress": "4 yards",
        "pillowcase": "1 yard"
    }
    return fabric_requirements.get(project_type, None)
while True:
    user_choice = input("What type of project are you making?(Skirt, dress or pillowcase)\nI'll tell you how many yards of fabric you need.\n").lower()
    result = calculate_fabric_needed(user_choice)
    #if the result is a valid response:
    if result:
        print(result)
        break
    else:
        print("Please type a valid response.")
