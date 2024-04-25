#pip install faker
from faker import Faker

fake = Faker()
name = set()

while len(name) < 80000:
    name.add(fake.name())

print(name)
