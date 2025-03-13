from arcgis.gis import GIS
from AGOL_Credentials import AGOLusername, AGOLpassword, AGOL_ORG

# Connect to ArcGIS Online
gis = GIS(AGOL_ORG, AGOLusername, AGOLpassword)

# Get the content item by its ID
item_id = "a7661bbffa6649cfbb0d09cd308b8eae"
item = gis.content.get(item_id)

# Get all properties of the content item
item_properties = item.properties

print('title: ', item.title)
print('snippet: ', item.snippet)
print('description: ', item.description)
print('tags: ', item.tags)
print('accessInformation: ', item.accessInformation)
print('licenseInfo: ', item.licenseInfo)
print('extent: ', item.extent)
print('sharing.groups: ', item.sharing.groups)

with open("license_info.py", "w") as file:
    file.write(item.licenseInfo)