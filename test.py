import os
import json

password = os.environ.get('PASSWORD')
api_key = os.environ.get('API_KEY')

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def count_vowels(text):
    if not text:
        return 0
    vowels = "aeiou"
    vowel_count = 0
    for character in text:
        if character in vowels:
            vowel_count += 1
    return vowel_count

def get_grade(score):
    if not isinstance(score, (int, float)):
        return None
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "F"
    return grade

def read_config(filename):
    if not filename:
        return ""
    with open(filename, "r") as file:
        content = file.read()
    return content

def add_item(item, cart=None):
    if cart is None:
        cart = []
    if not item:
        return cart
    cart.append(item)
    return cart

def first_item(items):
    if not items:
        return None
    return items[0]

print(count_vowels("hello"))
print(get_grade(95))