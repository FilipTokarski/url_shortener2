import string
import random


def generate_random_url(length=4):
    random_letters = list(random.choice(string.ascii_letters) for i in range(length))
    random_numbers = random.sample(range(100), length)
    zipped = zip(random_letters, random_numbers)
    random_list = [str(c) for element in zipped for c in element]
    full_string = ''.join(random_list)
    return full_string
