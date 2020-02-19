import xml.etree.ElementTree as ET
import re

tree = ET.parse('xml/Ready_To_Print_Release.xml')
root = tree.getroot()
#root2 = ET.fromstring(data)
#print(root.tag)
#print(root.attrib)

fonts = []
lists = []
styles = []
docPr = []
body = []

for i in root:
	print(i.tag)
	if (re.search("fonts",i.tag)!=None):
		fontsName = i.tag
		#print(i.keys)
		#print(i.items())
		print(len(i))
		print(i[0], '\n', i[0].tag, '\n', i[0].attrib, '\n', i[0].items())
	if (re.search("lists",i.tag)!=None):
		listsName = i.tag
	if (re.search("styles",i.tag)!=None):
		stylesName = i.tag
	if (re.search("docPr",i.tag)!=None):
		docPrName = i.tag
	if (re.search("body",i.tag)!=None):
		bodyTagName = i.tag

# перебор всех элементов
for child_of_root in root.iter(fontsName):
#for child_of_root in root.iter():
#for child_of_root in root.iter(bodyTagName):
	print(child_of_root.tag, child_of_root.keys(), child_of_root.items(), child_of_root.text)

'''
for i in root[0]:
	print(i.tag, i.attrib)
	print(i.text)
	print(i.getchildren())
'''
