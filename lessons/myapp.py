# Python XML Parsing
import xml.etree.ElementTree as ET
root = ET.parse('sample.xml').getroot()
#print(root)
tag = root.tag
print(tag)

# get all attributes
# attributes = root.attrib
# print(attributes)

# print(type(attributes))
# # extract a particular attribute
# year = attributes.get('year')
# print(attributes['year'])
# print('year : ',year)

# for holiday in root.findall('holiday'):
#     print(holiday)

# # iterate over child nodes
# for holiday in root.findall('holiday'):
 
#     # get all attributes of a node
#     attributes = holiday.attrib
#     print(attributes)
 
#     # get a particular attribute
#     attr_type = attributes.get('type')
#     print(attr_type)

for holiday in root.findall('holiday'):
 
    # access element - name
    name = holiday.find('name').text
    print(name)

    # access element - date
    date = holiday.find('date').text
    print('date : ', date)