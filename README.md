Project Title
SDE to AGO update Script

Description
Syncs local data with ArcGIS Online layer. Uses local ArcGIS Pro project.

all parameters are strings. 
rel_path : Local path where the project is located, e.g. C:\Temp
aprx_file : Name of the project. e.g. zoning.aprx 
map_in_aprx : Name of the map inside the arcgis pro project. e.g. Map
user: The username used to login to AGO
pass:word: The password used to login to AGO
ago_folder_name: Folder name where the layer is located. Leave blank ("") if it is at the root. e.g. "Transportation"
sd_fs_name: Name of the layer on AGO. e.g. "Zoning"
summary: Summary details of the AGO layer. e.g. "This is the transportation layer of COL"
tags: Tags of the AGO layer. e.g. "zoning"
description: Description details of the AGO layer. e.g. "This layer demonstrates the streets, DCTA Stations of the COL