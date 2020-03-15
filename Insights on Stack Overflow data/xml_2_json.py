
#pip install xmltodict
import xmltodict
import json
import sys
import re

#open xml file and parsing the xml
with open(sys.argv[1]) as fd:
    doc = xmltodict.parse(fd.read())
#output file
file=open(sys.argv[1].split(".xml")[0]+".csv", "a+")

#function to convert cammel case to snake case
def convert(name):
    name=name.split("@")[1]
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

count=0
for i in doc:
    dict1=doc[i]
    print(len(dict1))
    for k in dict1:
        dict2=dict1[k]
        for row in dict2:
            dict_to_dump={}
            #iterating over ever attribute of xml row
            for attr in row:
                dict_to_dump[convert(attr)]=row[attr]
            json.dump(dict_to_dump,file)
            file.write("\n")
            count += 1
            if count % 100000 == 0:
                print(count)
