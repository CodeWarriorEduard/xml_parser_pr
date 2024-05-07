import customtkinter
from customtkinter import filedialog
from parserXML import *
import os

dir = os.getcwd()
print(dir)

header_color = "#014955"

class XmlGui(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("XML Parser")
        self.geometry(f"1270x695+0+0")
        self.header = customtkinter.CTkFrame(self, fg_color=header_color)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.2)
        header_text = "XML PARSER"
        self.header_label = customtkinter.CTkLabel(self.header, text=header_text, font=("Open Sans", 24))
        self.header_label.place(relx=0.5, rely=0.5, anchor="center")

        # Contenedor de inputs
        self.container = customtkinter.CTkFrame(self)
        self.container.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)
        # Creacion de inputs
        #Input 1
        self.input1 = customtkinter.CTkTextbox(self.container)
        self.input1.place(relx=0.05, rely=0.1, relwidth=0.4, relheight=0.6)
        # Label Input 1
        title_label1 = customtkinter.CTkLabel(self.container, text="Escribe tu XML Aquí:")
        title_label1.place(relx=0.05, rely=0.05, anchor="w")
        # Input 2
        self.input2 = customtkinter.CTkTextbox(self.container)
        self.input2.place(relx=0.55, rely=0.1, relwidth=0.4, relheight=0.6)
        # Label Input 2
        title_label1 = customtkinter.CTkLabel(self.container, text="Output:")
        title_label1.place(relx=0.55, rely=0.05, anchor="w")

        #Run button
        self.button1 = customtkinter.CTkButton(self.container, text="Run", fg_color=header_color, command=self.getXmlnParse)
        self.button1.place(relx=0.25, rely=0.9, anchor="center")

        #Clear button
        self.button2 = customtkinter.CTkButton(self.container, text="Clear inputs", fg_color=header_color, command=self.clearInputs)
        self.button2.place(relx=0.75, rely=0.9, anchor="center")

        #Select file button
        self.button3 = customtkinter.CTkButton(self.container, text="Open XML file",fg_color=header_color, command=self.selectFile)
        self.button3.place(relx=0.50, rely=0.9, anchor="center")

    def selectFile(self):
        fileA = filedialog.askopenfilename(initialdir=dir, filetypes=[("XML files", "*.xml")])
        if fileA:
            with open(fileA, 'r') as f:
                content = f.read()
                self.input1.delete("1.0","end")
                self.input1.insert("end", content)


    def parseXML(self, text):
        parser = XMLParser(text)
        parser.parse()
        error = parser.error
        str_xml = ""
        if error == None:
            root = parser.get_root()
            str_xml = f"{root.tag} {{\n"
            for item in parser.get_elements():
                str_xml += f"\t{item.tag} {{\n"
                str_xml += f"\t\tatributos = {parser.get_attributes(item)}\n"
                str_xml += f"\t\ttext = {parser.get_text(item)}\n"
                str_xml += "\t\tchilds = {\n"
                for child in parser.get_children(item):
                    str_xml += f"\t\t\t{child.tag} {{\n"
                    str_xml += f"\t\t\t\tatributos = {parser.get_attributes(child)}\n"
                    str_xml += f"\t\t\t\ttext = {parser.get_text(child)}\n"
                    str_xml += "\t\t\t}\n"
                str_xml += "\t\t}\n"
                str_xml += "\t}\n"
            str_xml += "}\n"
        else:
            str_xml = str(error)
        return str_xml


    def getXmlnParse(self):
        inputtext = self.input1.get("1.0", "end-1c")
        parse = self.parseXML(inputtext)
        self.input2.delete("1.0", "end")
        self.input2.insert("end", parse)

    def clearInputs(self):
        self.input2.delete("1.0", "end")
        self.input1.delete("1.0", "end")

app = XmlGui()
app.mainloop()