import class_person

name = "Pattaraporn  Chawakijsophon"
age = 22
address = "Vietnam"

person = class_person.Person(name, age, address)

print(person.get_name())
print(person.get_age())
print(person.get_address())
print(person.get_info())