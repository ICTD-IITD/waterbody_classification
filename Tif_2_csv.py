from osgeo import gdal
import pandas as pd
import numpy as np
import os
import csv

import matplotlib.pyplot as plt

ds = gdal.Open("SL_STJamui_2021_01.tif")
print(ds)
# ds = gdal.Open("Months/sentinel2a_Jamui_2021_01.tif")

# TIFF to CSV 
# first option
xyz = gdal.Translate("dem.xyz", ds)
print(xyz)
xyz = None


df = pd.read_csv("dem.xyz", sep = " ", header = None)

print(df)

df.columns = ["x","y", "value"]
# df.to_csv("dem.csv", index = False)months =['01','02','03','04','05','09','10','11','12']

# for month in months:
#     ds = gdal.Open(f"Months/sentinel2a_Jamui_2021_{month}.tif") 
#     ar = ds.GetRasterBand(1).ReadAsArray()
#     flat = ar.flatten()
#     df[month] = flat
    
# df = df[df['value'] == 2]


# # df.drop('value', inplace=True, axis=1)

# months =['01','02','03','04','05','09','10','11','12']

# for month in months:
#     ds = gdal.Open(f"Months/sentinel2a_Jamui_2021_{month}.tif") 
#     ar = ds.GetRasterBand(1).ReadAsArray()
#     flat = ar.flatten()
#     df[month] = flat
    
# df = df[df['value'] == 2]

df.to_csv("SL_STJamui_2021_01.csv", index = False)

    

# ds = gdal.Open("dem.tif")


# for i in range(1, ds.RasterCount + 1):
#     ar = ds.GetRasterBand(i).ReadAsArray()
#     flat = ar.flatten()
    
#     df[ds.GetRasterBand(i).GetDescription()] = flat
#     print(ds.GetRasterBand(i).GetDescription())
    # flat = flat[~np.isnan(flat)] 



    # print(flat)

# df.to_csv("months.csv", index = False)


# bands = {ds.GetRasterBand(i).GetDescription(): i for i in range(1, ds.RasterCount + 1)}
# print(bands)


# for i in range(1, ds.RasterCount + 1):
#     ar = ds.GetRasterBand(i).ReadAsArray()
#     flat = ar.flatten()
#     flat = flat[~np.isnan(flat)] 



#     print(flat)

# gt = ds.GetGeoTransform()
# res = gt[1]
# xmin = gt[0]
# ymax = gt[3]
# xsize = ds.RasterXSize
# ysize = ds.RasterYSize
# xstart = xmin +res/2
# ystart = ymax - res/2
# # ds = None

# x = np.arange(xstart, xstart+xsize*res, res)
# y = np.arange(ystart, ystart-ysize*res, -res)
# x = np.tile(x, ysize)
# y = np.repeat(y, xsize)

# ar = ds.GetRasterBand(1).ReadAsArray()
# flat = ar.flatten()

# print(len(x))
# print(len(y))
# print(len(flat))

# dfn = pd.DataFrame({"x":x, "y":y, "value":flat})
