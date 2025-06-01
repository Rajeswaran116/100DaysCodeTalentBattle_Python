class Isosceles:
    def Itriangle(self):
        print("I am Isoscles Triangle")

class Equi(Isosceles):
    def Etriangle(self):
        print("I am Equi Triangle")

class C(Equi):
    def Triangle(self):
        print("I am Trinagle")

d=C()
d.Etriangle()
d.Itriangle()
d.Triangle()
