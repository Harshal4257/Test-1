import os

password = os.environ.get('PASSWORD')

def count_vowels(input_string):
    if not isinstance(input_string, str):
        return 0
    count = 0
    for char in input_string:
        if char in "aeiou":
            count += 1
    return count

def get_grade(student_score):
    if not isinstance(student_score, (int, float)) or student_score < 0 or student_score > 100:
        return "Invalid score"
    if student_score >= 90:
        grade = "A"
    elif student_score >= 80:
        grade = "B"
    else:
        grade = "F"
    return grade

def read_config(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except Exception as e:
        return str(e)

def add_item(product, cart=None):
    if cart is None:
        cart = []
    if not isinstance(cart, list):
        cart = []
    if not isinstance(product, str):
        product = str(product)
    cart.append(product)
    return cart

print(count_vowels("hello"))
print(get_grade(95))