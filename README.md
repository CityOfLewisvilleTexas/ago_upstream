SDE to AGO Update Script
Description
This script syncs local data with an ArcGIS Online (AGO) layer, using a local ArcGIS Pro project.

Parameters
Parameter	Type	Description	Example
rel_path	string	Local path where the project is located.	C:\Temp
aprx_file	string	Name of the ArcGIS Pro project file.	zoning.aprx
map_in_aprx	string	Name of the map inside the ArcGIS Pro project.	Map
user	string	The username used to login to AGO.	your_username
password	string	The password used to login to AGO.	your_password
ago_folder_name	string	The AGO folder where the layer is located. Leave blank ("") if it's at the root level.	"Transportation"
sd_fs_name	string	The name of the feature service (layer) on AGO.	Zoning
summary	string	Summary details of the AGO layer.	This is the transportation layer of COL
tags	string	Tags associated with the AGO layer.	zoning
description	string	Description details of the AGO layer.	This layer demonstrates the streets, DCTA Stations of the COL
share_organization	boolean	If the layer should be shared with the organization. Defaults to True.	True
share_everyone	boolean	If the layer should be shared with everyone. Defaults to False.	False
