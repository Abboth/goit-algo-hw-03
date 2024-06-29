#task № 2 in first homework

import re

def normalize_phone(phone_number:str)->str: #приводим номера телефонов к единому нужному формату

    phone_number = re.sub(r"[\D]", "",phone_number)
    pattern = r"(\d{4})(\d{3})(\d{3})"
    correct_format = r"+38\1\2\3"

    while len(phone_number) > 10:
        phone_number = phone_number[1:]

    formatted_phone_number = re.sub(pattern, correct_format, phone_number)
    return formatted_phone_number

print(normalize_phone(phone))