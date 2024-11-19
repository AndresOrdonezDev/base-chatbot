import pickle as pk
from car import Car

car1 = Car('Mazda', 2021, 15000)
car2 = Car('Renault', 2020, 12000)
car3 = Car('KIA', 2019,10000)

list_cars = [car1, car2, car3]

file_binary = open('list_cars', 'wb')

pk.dump(list_cars, file_binary)

file_binary.close()

del(file_binary)

