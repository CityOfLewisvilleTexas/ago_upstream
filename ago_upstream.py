# Important Notes 
# Before importing libraries, make sure you are logged into ArcGIS Pro with sign me automatically checked.
# If you have problem with loading the login page, and if it is internet explorer security blocks,
# Then add www.arcgis.com and js.arcgis.com to the trusted sites.
# Check whether the latest ArcGIS version is installed.
import os
import arcpy
import ago_classes
from arcgis.gis import GIS

def update_hosted_service(rel_path, aprx_file, map_in_aprx, user, password, ago_folder_name, sd_fs_name, summary, tags, description):
    '''
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
        description: Description details of the AGO layer. e.g. "This layer demonstrates the streets, DCTA Stations of the COL"
    '''
    prj = arcpy.mp.ArcGISProject(aprx_file)
    m = prj.listMaps(map_in_aprx)[0]
    print("map  ----", m)
    for lyr in m.listLayers():
        print(lyr)

    portal = "http://www.arcgis.com"
    # Set sharing options
    shrOrg = True
    shrEveryone = False
    shrGroups = ""

    sd_draft = os.path.join(rel_path, sd_fs_name + ".sddraft")
    sd = os.path.join(rel_path, sd_fs_name + ".sd")
    print(rel_path)
    print(sd_draft)
    print(sd)

    # Create a new SDDraft and stage to SD
    print("Creating SD file")
    arcpy.env.overwriteOutput = True
    mp = prj.listMaps()[0]

    print(mp)
    print(sd_draft)
    print(sd_fs_name)

    arcpy.mp.CreateWebLayerSDDraft(mp, sd_draft, sd_fs_name, 'MY_HOSTED_SERVICES', 'FEATURE_ACCESS', ago_folder_name, True, True)
    arcpy.StageService_server(sd_draft, sd)

    print("Connecting to {}".format(portal))
    gis = GIS(portal, user, password)

    # Find the SD, update it, publish /w overwrite and set sharing and metadata
    print("Search for original SD on portal…")
    sdItemList = gis.content.search("{} AND owner:{}".format(sd_fs_name, user), item_type="Service Definition", max_items=3)
    print('Total found sd item {}'.format(len(sdItemList)))
    for sd_item in sdItemList:
        print('Name of the service {}'.format(sd_item.title))

    for sdItem in sdItemList:
        print("Found SD: {}, ID: {} ".format(sdItem.title, sdItem.id))
        if(sdItem.title == sd_fs_name):
            print("Matching SD: {}, with searched FS {} ".format(sdItem.title, sd_fs_name))
            # Create Feature Service SharingDraft and set service properties
            sharing_draft = mp.getWebLayerSharingDraft("HOSTING_SERVER", "FEATURE", sd_fs_name)
            sharing_draft.summary = summary
            sharing_draft.tags = tags
            sharing_draft.description = description
            sharing_draft.credits = ""
            sharing_draft.useLimitations = ""

            # Create Service Definition Draft file
            sharing_draft.exportToSDDraft(sd_draft)
            # Stage Service
            try:
                arcpy.StageService_server(sd_draft, sd)
                warnings = arcpy.GetMessages(1)
                print(warnings)
            except Exception as stage_exception:
                print("Sddraft not staged. Analyzer errors encountered - {}".format(str(stage_exception)))

            print("Updating data --- sdItem.update…")
            sdItem.update(data=sd)

            print("preserving EditUsers And Timestamps to true")
            pub_params = {"editorTrackingInfo" : {"enableEditorTracking":'true', "preserveEditUsersAndTimestamps":'true'}}
            fs = sdItem.publish(publish_parameters=pub_params, overwrite=True)

            print("Overwriting the service --- sdItem.publish…")
            fs = sdItem.publish(overwrite=True)

            if shrOrg or shrEveryone or shrGroups:
                print("Setting sharing options…")
                fs.share(org=shrOrg, everyone=shrEveryone, groups=shrGroups)

            print("Finished updating: {} – ID: {}".format(fs.title, fs.id))
            break

        else:
            print("Found SD: {}, is not the same as searched FS {}".format(sdItem.title, sd_fs_name))
            print('Skipping to the next item, if not exiting.')

    del m
    del mp
    del prj
    print("lock files deleted.")

def main():
    arcgis_project = ago_classes.arcgis_project
    ago_object = ago_classes.ago_object
    
    try:
        rel_path = r"C:\Temp"
        local_project = arcgis_project(rel_path=rel_path,
                                            aprx_file=os.path.join(rel_path,"PROJECT.aprx"),
                                            map_in_aprx="MAP")
        
        ago_object = ago_object(user="USERNAME", password="PASSWORD",
                                    ago_folder_name="", sd_fs_name="Layer_Name_on_AGO",
                                    summary="Summary", tags="Tags", 
                                    description="Description")

        print(f"Project file : {local_project.aprx_file}")
        aprx_to_save = arcpy.mp.ArcGISProject(local_project.aprx_file)
        aprx_to_save.save()
        print(local_project.aprx_file, " is saved")

        update_hosted_service(rel_path=local_project.rel_path, aprx_file=local_project.aprx_file, 
                              map_in_aprx=local_project.map_in_aprx, user=ago_object.user, password=ago_object.password,
                              ago_folder_name=ago_object.ago_folder_name, 
                              sd_fs_name=ago_object.sd_fs_name, summary=ago_object.summary, 
                              tags=ago_object.tags, description=ago_object.description)
        
        del local_project.aprx_file
        
    except:
        print("Error saving or publishing..")
        del local_project.aprx_file

if __name__ == '__main__':
    main()