from faker import Faker

fake = Faker()

# while True: 
#   print(fake.name())


print(fake.name() + ": " + fake.text())