import xml.etree.ElementTree as ET
tree = ET.parse('input.xml')
root = tree.getroot()
print (root)