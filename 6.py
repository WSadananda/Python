class Car:
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

Carobj=Car("Car","V1","2015")
print(Carobj.brand,Carobj.model,Carobj.year)

