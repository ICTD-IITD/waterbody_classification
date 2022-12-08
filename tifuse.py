from dis import dis
from osgeo import gdal
import os, sys
import imageio
import numpy as np
from PIL import Image

# load GDAL (Geospatial Data Abstraction Library) driver for tiff files
driver = gdal.GetDriverByName('GTiff')