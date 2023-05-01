import csv

#використання функцію  DictReader() модуля csv
with open('programmers.csv', 'rt') as freading:
    creading = csv.DictReader(freading, fieldnames=['language', 'developer']) #використовуючи нову функцію DictReader() і вказуючи імена колонок:
    print(type(creading))
    programmers = [row for row in creading]
print(programmers)
print("*"*34)

#використання функцію  DictReader() модуля csv не враховуючи fieldnames
with open('programmers.csv', 'rt') as freading:
    creading = csv.DictReader(freading)
    programmers = [row for row in creading]
print(programmers)
