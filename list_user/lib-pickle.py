#pickle => library for serializing data
import pickle as pk
name_list = ['Pedro', 'Ana', 'María', 'Juan' ]

binary_file =  open('name_list', 'wb') #crear archivo

pk.dump(name_list, binary_file)

binary_file.close()
del(binary_file)#delete binary file from memory => hablar sobre que es memoria

# open saved list
open_file = open('name_list', 'rb')

loaded_list = pk.load(open_file)

print(loaded_list)