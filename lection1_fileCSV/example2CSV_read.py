import csv

#використання функції  reader() модуля csv
with open('programmers.csv', 'rt') as file: # менеджер контексту
    # creading = csv.reader(file, delimiter=";")
    creading = csv.reader(file)
    print(type(creading))
    programmers = [row for row in creading] # фрмування списку із використанням включення у список
    # programmers=[]
    # for row in creading:
    #     #print(row) - перевірити чи row не = '[]'
    #     if len(row)!=0:
    #         programmers.append(row)
print(programmers)


