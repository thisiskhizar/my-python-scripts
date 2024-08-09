import csv
from faker import Faker
import random

fake = Faker()

filename = 'students.csv'
num_records = 100

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "first_name", "last_name", "email", "date_of_birth", "enrollment_date", "is_active"])

    for i in range(1, num_records + 1):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=24)
        enrollment_date = fake.date_this_decade()
        is_active = random.choice([True, False])

        writer.writerow([i, first_name, last_name, email, date_of_birth, enrollment_date, is_active])

print(f"{num_records} records have been written to {filename}")
