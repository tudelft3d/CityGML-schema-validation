#!/usr/bin/env python

import sys
import os
import glob
from lxml import etree


def main():
    if len(sys.argv) != 2:
        print "Error: you must give one CityGML document as input or a folder."
        sys.exit()
    if (os.path.isdir(sys.argv[1]) == True):
        validateallinfolder(sys.argv[1])
    else:
        validateonefile(sys.argv[1])


def validateonefile(fIn):
    doc, xsd = getXML(fIn)
    if (doc == None) and (xsd == None):
        print "Invalid CityGML document: not a CityGML document."
        sys.exit()
    xmlschema = etree.XMLSchema(xsd)
    valid = doc.xmlschema(xsd)
    if valid == True:
        print "Document is valid."
    else:
        try:
            xmlschema.assert_(doc)
        except etree.XMLSyntaxError as e:
            print "Invalid document"
            print "Error", e
            log = xmlschema.error_log
            print log
        except AssertionError as e:
            print "INVALID DOCUMENT"
            print "================"
            print e


def validateonefiletruefalse(fIn):
    try:
        doc, xsd = getXML(fIn)
        if (doc == None) and (xsd == None):
            return False
    except:
        return False
    return doc.xmlschema(xsd)


def validateallinfolder(myfolder):
    myfiles = []
    for root, dirnames, filenames in os.walk(myfolder):
        myfiles.extend(glob.glob(root + "/*.xml"))
    for root, dirnames, filenames in os.walk(myfolder):
        myfiles.extend(glob.glob(root + "/*.gml"))
    myresults = []
    for f in myfiles:
        if validateonefiletruefalse(f) == True:
            myresults.append(True)
        else:
            myresults.append(False)    
    valid = 0
    # for i,f in enumerate(myfiles):
    #     print f
    #     if myresults[i] == True:
    #         print 1
    #         valid += 1
    #     else:
    #         print 0
    print myfolder, valid, "/", len(myfiles)
    # print "**********"
    # print "Summary: ", valid, "/", len(myfiles), "valid files."
    # print "**********"


def getXML(fIn):
    parser = etree.XMLParser(ns_clean=True)
    doc = etree.parse(fIn)    
    root = doc.getroot()
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
                citygmlversion = '2.0'
                break
    if citygmlversion == "":
        return None, None
    if citygmlversion == "0.4":
        xsd = etree.parse("./schemas/v0.4/CityGML.xsd")
    elif citygmlversion == "1.0":
        xsd = etree.parse("./schemas/v1.0/CityGML.xsd")
    else:
        xsd = etree.parse("./schemas/v2.0/CityGML.xsd")
    return doc, xsd




if __name__ == '__main__':
    main()