from pathlib import Path
from pprint import pprint
import os
from ost import Sentinel1Scene
import os


cdir = os.path.abspath(os.getcwd())

# create a processing directory
output_dir = cdir + '/SARS_data'
os.makedirs(output_dir,exist_ok=True)
# print(str(output_dir))

scene_id = "S1A_IW_GRDH_1SDV_20141003T040550_20141003T040619_002660_002F64_EC04"
s1 = Sentinel1Scene(scene_id)
s1.info()

s1.download(output_dir)

s1.create_rgb(outfile=output_dir / f"{s1.start_date}.tif")

print(" The path to our newly created RGB product can be obtained the following way:")
s1.ard_rgb

path_to_thumbnail = output_dir / f"{s1.start_date}.TN.jpg"

# create the thumbnail image
s1.create_rgb_thumbnail(outfile=str(path_to_thumbnail))