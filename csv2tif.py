import pandas as pd
from osgeo import gdal


ds = gdal.Open("classes.tif")
# ds = gdal.Open("Months/sentinel2a_Jamui_2021_01.tif")

# TIFF to CSV 
# first option
xyz = gdal.Translate("dem.xyz", ds)
xyz = None

df1 = pd.read_csv("dem.xyz", sep = " ", header = None)
df1.columns = ["x","y", "value"]
df1.drop('value', inplace=True, axis=1)




df = pd.read_csv('map.csv')
# df_all = pd.read_csv('map.csv')
df.drop('index', inplace=True, axis=1)

dall = pd.merge(df1, df, how="left",left_on=['x','y'], right_on = ['x','y'])

dall['value'] = dall['value'].fillna(2)

print(dall)

dall.to_csv("map.xyz", index = False, header = None, sep = " ")
demn = gdal.Translate("map.tif", "map.xyz", outputSRS = "EPSG:32719")
demn = None


