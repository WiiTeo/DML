# DreamML Project
# wiiteo.github.io/dml
# By WiiTeo

# Lib

#--------------------------------------------------
import os
import sys
import xml.etree.ElementTree as ET
import dml
from dml import *
#--------------------------------------------------
tree = ET.parse(sys.argv[1])
root = tree.getroot()
#--------------------------------------------------
for dmlf in root:

    if dmlf.tag == S1:
        print(dmlf.text)

    elif dmlf.tag == S2:
        os.system(dmlf.text)

    elif dmlf.tag == S3:
        exit()

    else:
        dml.DML.Error(dmlf.tag + ": is not a valid syntax (Content of " + dmlf.tag + " = " + dmlf.text + ")")
#--------------------------------------------------