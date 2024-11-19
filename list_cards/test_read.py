import pickle as pk 

open_file = open('list_cars','rb')

loaded_cars = pk.load(open_file)

for c in loaded_cars:
    c.show()