import xml.dom.minidom
from xml.dom.minidom import parse

DOMTree = xml.dom.minidom.parse('exam.xml')

doc = DOMTree.documentElement

