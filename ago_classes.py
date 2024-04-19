# Creates classes for the AGO Upstream tool
class arcgis_project:
    def __init__(self, rel_path, aprx_file, map_in_aprx) -> None:
        self.rel_path = rel_path
        self.aprx_file = aprx_file
        self.map_in_aprx = map_in_aprx


class ago_object:
    def __init__(self, user, password, ago_folder_name, sd_fs_name, summary, tags, description) -> None:
        self.user = user
        self.password = password
        self.ago_folder_name = ago_folder_name
        self.sd_fs_name = sd_fs_name
        self.summary = summary
        self.tags = tags
        self.description = description