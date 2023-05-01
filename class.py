class Alpha:
    def hi():
        print("class Alpha")

class Bravo:
    def hi():
        print("class Bravo")

class Charlie:
    def hi():
        print("class Charli")

class Delta(Alpha):
    pass

class Echo(Delta):
    pass

class Foxtrot(Bravo,Alpha):
    pass

class Golf(Foxtrot):
    pass

class Hotel(Echo, Charlie, Golf):
    pass

Alpha.hi()
Delta.hi()
Golf.hi()
Hotel.hi()
