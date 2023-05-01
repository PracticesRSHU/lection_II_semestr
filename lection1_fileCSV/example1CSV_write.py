import csv
programmers = [
    ['Python', 'Guido van Rossum'],
    ['Scala', 'Martin Odersky'],
    ['PHP', 'Rasmus Lerdorf'],
    ['Ruby', 'Yukihiro Matsumoto'],
    ['C', 'Dennis Ritchie'],
]
with open('programmers.csv', 'wt') as frecord: # менеджер контексту
    csvrecord = csv.writer(frecord)
    # csvrecord = csv.writer(frecord, dialect='excel-tab', delimiter=';')
    csvrecord.writerows(programmers)
    # csvrecord.writerows()
