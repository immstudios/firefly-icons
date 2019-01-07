#!/usr/bin/env python3

import os

from xml.etree import ElementTree as ET

r = ET.XML(open("icons.svg").read())

for g in r.findall("{http://www.w3.org/2000/svg}g"):
    id = g.attrib["id"]
    label = g.attrib["{http://www.inkscape.org/namespaces/inkscape}label"]
    path = "export/{}.png".format(label)
    cmd = "inkscape --export-png={} --export-area-page -w 24 -h 24 --export-id={} --export-id-only icons.svg".format(path, id)
    print (cmd)
    os.system(cmd)
    path = "export/{}-sm.png".format(label)
    cmd = "inkscape --export-png={} --export-area-page -w 16 -h 16 --export-id={} --export-id-only icons.svg".format(path, id)
    print (cmd)
    os.system(cmd)
