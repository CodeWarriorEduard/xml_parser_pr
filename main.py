from parser import XMLParser

def main():
    parser = XMLParser('./test.xml')
    root = parser.get_root()
    items = parser.get_elements()
    print(f"{root.tag} {{")
    for item in items:
        print(f"\t{item.tag} {{")
        print("\t\tatributos = ", parser.get_attributes(item))
        print("\t\ttext = ", parser.get_text(item))
        children = parser.get_children(item)
        print("\tchilds = {")
        for child in children:
            print(f"\t\t{child.tag} {{")
            print("\t\t\tatributos = ", parser.get_attributes(child))
            print("\t\t\ttext = ", parser.get_text(child))
            print("\t\t\t}")
        print("\t\t}")
        print("\t}")
    print(f"}}")
if __name__ == '__main__':
    main()



