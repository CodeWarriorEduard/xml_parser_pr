import xml.etree.ElementTree as ET


class XMLParser:
    def __init__(self, fileXml):
        self.fileXml = fileXml
        self.tree = None

    def parse(self):
        self.tree = ET.parse(self.fileXml)

    def get_root(self):
        if self.tree is None:
            self.parse()
        return self.tree.getroot()

    def get_elements(self, tag=None):
        root = self.get_root()
        if tag:
            return root.findall('.//'+tag)
        else:
            return list(root)

    def get_attributes(self, element):
        return element.attrib

    def get_text(self, element):
        return element.text

    def get_children(self, element):
        return list(element)
