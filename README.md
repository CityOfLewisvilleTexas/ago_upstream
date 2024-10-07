# **SDE to AGO Update Script**

## **Description**
This script syncs local data with an ArcGIS Online (AGO) layer, using a local ArcGIS Pro project.

---

## **Parameters**

- **`rel_path`** (string):  
  Local path where the project is located.  
  **Example:** `C:\Temp`

- **`aprx_file`** (string):  
  Name of the ArcGIS Pro project file.  
  **Example:** `zoning.aprx`

- **`map_in_aprx`** (string):  
  Name of the map inside the ArcGIS Pro project.  
  **Example:** `Map`

- **`user`** (string):  
  The username used to log in to AGO.  
  **Example:** `your_username`

- **`password`** (string):  
  The password used to log in to AGO.  
  **Example:** `your_password`

- **`ago_folder_name`** (string):  
  The AGO folder where the layer is located. Leave blank (`""`) if it's at the root level.  
  **Example:** `"Transportation"`

- **`sd_fs_name`** (string):  
  The name of the feature service (layer) on AGO.  
  **Example:** `Zoning`

- **`summary`** (string):  
  Summary details of the AGO layer.  
  **Example:** `This is the transportation layer of COL`

- **`tags`** (string):  
  Tags associated with the AGO layer.  
  **Example:** `zoning`

- **`description`** (string):  
  Description details of the AGO layer.  
  **Example:** `This layer demonstrates the streets, DCTA Stations of the COL`

- **`share_organization`** (boolean):  
  If the layer should be shared with the organization.  
  **Default:** `True`

- **`share_everyone`** (boolean):  
  If the layer should be shared with everyone.  
  **Default:** `False`

---

## **Usage Example**

```python
# Example of how to call the function with parameters
sync_data_with_ago(
    rel_path="C:\\Temp",
    aprx_file="zoning.aprx",
    map_in_aprx="Map",
    user="your_username",
    password="your_password",
    ago_folder_name="Transportation",
    sd_fs_name="Zoning",
    summary="This is the transportation layer of COL",
    tags="zoning",
    description="This layer demonstrates the streets, DCTA Stations of the COL",
    share_organization=True,
    share_everyone=False
)
