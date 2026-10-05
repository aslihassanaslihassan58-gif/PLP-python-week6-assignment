from safe_tools import safe_divide, safe_number, get_field

print("This program never crashes!")
print(safe_divide(10, 2))
print(safe_divide(10, 0))

name = input("Enter a number: ")
print(safe_number(name))

learner = {"name": "Amina", "score": 82}
print(get_field(learner, "score"))
print(get_field(learner, "email"))