# DreamML Project
# dream-ml.is-great.org
# By TO_ (Téo)

# MIT OpenSource Licence

import os
import sys
import xml.etree.ElementTree as ET
import dml
from dml import *

tree = ET.parse('Example.dml')
root = tree.getroot()

for dmlf in root:
    if root.tag == "Dream":
        if root[0][0].tag == "Print":
            print(root[0][0].text)
            exit()
        if root[0][0].tag == "CMD":
            os.system(root[0][0].text)
            exit()
        else:
            DML_Error(root[0][0].tag + ": is not a valid syntax")
            exit()