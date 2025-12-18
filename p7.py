class Car:
  def _init_(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year

  def describe_car(self):
    print('make' {self.make} ', model' {self.model} ', year' {self.year})

car1 = ('Toyota', 'Corolla', 2020)

car1.describe_car
