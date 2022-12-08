from dis import dis
from osgeo import gdal
import os, sys
import geopandas as gpd
import imageio
import numpy as np
from PIL import Image
import rasterio
from rasterio import features
import itertools


def get_coord(district,main_folder):
    """
    For a given district, it looks in the main folder for a tif file. Extracts the coordinates from it, and returns the bounding box as min x,y cordinates and max x,y cordinates as a 4-tuple
    :param str district: District name
    :param str main_folder: Folder path with tif file
    """
    
    print(district)
    # Get one tif file of this district for reference. This can be the initial tif files downloaded from GEE 
    for infile in os.listdir(main_folder):
        if (infile[-4:] == ".tif"):
            filepath = main_folder+"/"+infile
            break
    
    with rasterio.open(filepath) as src:
        band=src.read()

        mask = band!= 0
        shapes = features.shapes(band, mask=mask, transform=src.transform)
        fc = ({"geometry": shape, "properties": {"value": value}} for shape, value in shapes)
        points = gpd.GeoDataFrame.from_features(fc)
        
        
        b = points[points.geometry.map(lambda z: True if not z.is_empty else False)].geometry.map(lambda z: z.exterior.xy).values

        x = [c[0] for c in b]
        x = list(itertools.chain.from_iterable(x))
        
        y = [c[1] for c in b]
        y = list(itertools.chain.from_iterable(y))
        
        print(min(x))
        print(min(y))
        print(max(x))
        print(max(y))

        return min(x),min(y),max(x),max(y)

            

if __name__ == "__main__":
    # districts for which coordinate is needed
    districts = ['Jamui']
    
    for district in districts:    
        main_folder = 'Classification_'+district
        path_for_final_prediction_pngs = main_folder
        get_coord(district,main_folder)
