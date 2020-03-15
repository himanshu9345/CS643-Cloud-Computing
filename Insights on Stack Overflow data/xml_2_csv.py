#pip install xmlutils
from xml.etree import ElementTree
import sys

#open xml file and parsing the xml
tree = ElementTree.parse(sys.argv[1]+".xml")
root = tree.getroot()
print("file read")
#output file
f=open(sys.argv[1]+".csv", "a+")
count=0
for el in tree.iter():
    str1=""
    dict1=el.attrib
    # iterating over ever attribute of xml row
    for i in dict1:
        str1+=dict1[i]+","
    f.write(str1[:-1]+"\n")
    f.flush()
    count+=1
    if count%100000==0:
        print(count)
