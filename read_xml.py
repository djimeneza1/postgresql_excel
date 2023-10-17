import xml.etree.ElementTree as et 

xtree = et.parse("Peru_Q1_2023.xml")
xroot = xtree.getroot()

print(xroot)
print(list(xroot)[0])
print(list(list(xroot)[0])[0])
print(list(list(list(xroot)[0])[0]))

print(len(list(xroot)))