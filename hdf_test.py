import pandas as pd
from pyhdf.SD import SD, SDC
import numpy as np
import matplotlib.pyplot as plt

from osgeo import gdal

file_name = 'cali_2018_data/MOD14A2.A2018145.h08v04.006.2018154000419.hdf'
file = SD(file_name, SDC.READ)
#dir(file)

print(file.info())

#xdim = file.select('XDim')

x=file.attributes()
for idx,sds in enumerate(x.keys()):
    print(idx,sds)
    print(file.attr(idx).info())
    print(file.attr(idx).get())
    #items in locations 1 and 13 have data
    #struct and archive metadata

datasets_dic = file.datasets()

for idx,sds in enumerate(datasets_dic.keys()):
    print(idx,sds)
    
UpperLeftPointMtrs=(-11119505.196667,5559752.598333)
LowerRightMtrs=(-10007554.677000,4447802.078667)


    
sds_obj = file.select('FireMask')
print(sds_obj.info())

data = sds_obj.get() # get sds data
print(data)

p = plt.pcolormesh(data)
plt.show()

import pprint

pprint.pprint( sds_obj.attributes() )

print(np.shape(data))

sds_obj_2 = file.select('QA')
data2 = sds_obj_2.get() # get sds data
print(data2)
pprint.pprint( sds_obj_2.attributes() )

##f = h5py.File("test3.hdf",'r')
##
###pd.read_hdf("test3.hdf")
##
##import tables
###file = tables.open_file('test2.hdf')
##

