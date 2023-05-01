import csv
programmers = [
    {'language': 'Python', 'developer': 'Guido van Rossum'},
    {'language': 'Scala', 'developer': 'Martin Odersky'},
    {'language': 'PHP', 'developer': 'Rasmus Lerdorf'},
    {'language': 'Ruby', 'developer': 'Yukihiro Matsumoto'},
    {'language': 'C', 'developer': 'Dennis Ritchie'},
]
headlist=['language', 'developer']
with open('programmers.csv', 'wt') as file:
    crecord = csv.DictWriter(file,headlist)
    crecord.writeheader()
    crecord.writerows(programmers)

# def ttt(ww):
#     return "sdfs"+str(ww)
# ttt(89)