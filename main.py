import random
import string

def generate_random_email():

    name_length = random.randint(5, 10)
    name = ''.join(random.choices(string.ascii_lowercase, k=name_length))

    domain_length = random.randint(3, 7)
    domain = ''.join(random.choices(string.ascii_lowercase, k=domain_length))

    local_length = random.randint(2, 3)
    local = ''.join(random.choices(string.ascii_lowercase, k=local_length))

    email = f"{name}@{domain}.{local}"
    return email

print(generate_random_email())