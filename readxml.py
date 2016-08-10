#coding=utf-8
import xml.etree.ElementTree as ET
import os

def readxml():
    object_name = "2009081097"
    fp = os.path.abspath("")
    print fp

    tree = ET.parse(fp+"/students.xml")

    root = tree.getroot()
    print root[1][3].tag
    print root[1][3].attrib
    print root[1][3].text
    child = root.find("student")
    no = child.get("no")
    print no

    for student in root:
        print student.tag,student.attrib

    for student in root.findall("student"):
        no = student.get("no")
        if no == object_name:
            name = student.find("name").text
            age = student.find("age").text
            gender = student.find("gender").text
            print no,name,age,gender



if __name__ =="__main__":
    readxml()