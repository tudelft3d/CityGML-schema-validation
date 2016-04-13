#!/usr/bin/env python

import sys
from lxml import etree

if len(sys.argv) != 2:
    print "Error: you must give one CityGML document as input."
    sys.exit()
fIn = sys.argv[1]

try:
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(fIn)    
    root = tree.getroot()
    citygmlversion = ""
    for key in root.nsmap.keys():
        if root.nsmap[key].find('www.opengis.net/citygml') != -1:
            if (root.nsmap[key][-3:] == '0.4'):
                citygmlversion = '0.4'
                break
            if (root.nsmap[key][-3:] == '1.0'):
                citygmlversion = '1.0'
                break
            if (root.nsmap[key][-3:] == '2.0'):
                citygmlversion = '2.4'
                break

    if citygmlversion == "":
        print "Document is invalid: CityGML namespace not found"
        sys.exit()
    if citygmlversion == "0.4":
        xsd = etree.parse("./schemas/v0.4/CityGML.xsd")
    elif citygmlversion == "1.0":
        xsd = etree.parse("./schemas/v1.0/CityGML.xsd")
    else:
        xsd = etree.parse("./schemas/v2.0/CityGML.xsd")
    xmlschema = etree.XMLSchema(xsd)
    xmlschema.assertValid(tree)
    print "Document is valid."

except etree.XMLSyntaxError as e:
    print "Invalid document"
    print "Error", e
    
except AssertionError as e:
    print "Invalid document", e

