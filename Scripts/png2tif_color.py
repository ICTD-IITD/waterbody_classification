from dis import dis
from osgeo import gdal
import os, sys
import imageio
import numpy as np
from PIL import Image

# load GDAL (Geospatial Data Abstraction Library) driver for tiff files
driver = gdal.GetDriverByName('GTiff')

def gettif(district,main_folder,path_for_final_prediction_pngs):
    """
    For a given district, it looks in the main folder for a tif file. Extracts the coordinates from it, and in the path_for_final_prediction_pngs converts pngs to tifs and save in a path_for_final_prediction_pngs/tif folder
    :param str district: District name
    :param str main_folder: Folder path with tif file
    :param str path_for_final_prediction_pngs: Folder path with png files to convert
    """
    
    print(district)
    # Get one tif file of this district for reference. This can be the initial tif files downloaded from GEE 
    for infile in os.listdir(main_folder):
        if (infile[-4:] == ".tif"):
            filepath = main_folder+"/"+infile
            break
    
    reference_image = gdal.Open(filepath)
    
    #1 because we have information in a single band (prediction classes) 
    pixel_predictions = (reference_image.GetRasterBand(1)).ReadAsArray()
    [cols, rows] = pixel_predictions.shape


    os.makedirs(path_for_final_prediction_pngs+'/tifs',exist_ok=True)
    
    for infile in os.listdir(path_for_final_prediction_pngs):
        if infile[-4:] == ".png":
            print(infile)
            
            pngImage = np.array( Image.open( path_for_final_prediction_pngs+'/'+infile ))
            print("The unique labels in png image are: ", np.unique(pngImage) )
            print("The shape of png image is: ", pngImage.shape )
            
            destination_filename = path_for_final_prediction_pngs+'/tifs/'+infile[:-4]+'.tif'
            
            
            #Setting the structure for the destination tif file
            dst_ds = driver.Create(destination_filename, rows, cols, 1, gdal.GDT_UInt16)
            dst_ds.SetGeoTransform(reference_image.GetGeoTransform())
            dst_ds.SetProjection(reference_image.GetProjection())
            
            # Basically tiff only takes 0 to 255 
            # Linear combination as 2D matrix is input
            data_array = (pngImage[:,:,0] + 6*pngImage[:,:,1] + pngImage[:,:,2])
            data_array_scaled = np.interp(data_array, (data_array.min(), data_array.max()), (0, 255))
            
            
            # dst_ds.GetRasterBand(1).WriteArray(pngImage)
            dst_ds.GetRasterBand(1).WriteArray(data_array_scaled)
            dst_ds.FlushCache()
            
            band = dst_ds.GetRasterBand(1)
            
            #making color
            colors = gdal.ColorTable()
            
            # Change RBG for different colors
            colors.CreateColorRamp(0, (0, 0, 0), 40, (0, 0, 255))
            colors.CreateColorRamp(40, (0, 0, 255) , 89, (255, 0, 0))
            colors.CreateColorRamp(89, (255, 0, 0), 181, (229, 245, 249))
            colors.CreateColorRamp(181, (229, 245, 249), 255, (0, 255, 0))

            band.SetRasterColorTable(colors)
            band.SetRasterColorInterpretation(gdal.GCI_PaletteIndex)
            
            #Checking the validity of created tif file
            tiffImage = np.asarray( Image.open(destination_filename) )
            print("The unique labels in tiff image are: ", np.unique(tiffImage) )
            print("The shape of tiff image is: ", tiffImage.shape )
            print('\n')
            

if __name__ == "__main__":
    # districts for which ground truth is available
    districts = ['Jamui']
    
    for district in districts:    
        main_folder = 'Classification_'+district
        path_for_final_prediction_pngs = main_folder
        # path_for_final_prediction_pngs = "Landcover_Predictions_Using_IndiaSat/"+district
        gettif(district,main_folder,path_for_final_prediction_pngs)

