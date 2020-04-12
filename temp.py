from pyhdf.SD import SD, SDC

file_name = 'test1.hdf'
file = SD(file_name, SDC.READ)

print(file.info())
