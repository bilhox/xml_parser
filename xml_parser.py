
class Stack :

    def __init__(self, size) :
        self.size = size
        self.contenu = []

    def stack_element(self, element) :
        if self.is_full() :
            print("Impossible, the stack is full !")
        else :
            self.contenu.append(element)

    def unstack_element(self) :
        if self.is_empty() :
            print("Impossible, the stack is empty !")
        else :
            return self.contenu.pop()

    def is_empty(self) :
        if self.contenu == [] :
            return True
        else :
            return False

    def is_full(self) :
        if len(self.contenu) >= self.size :
            return True
        else :
            return False

    def nbr_elements(self) :
        return len(self.contenu)

class Tree():

    def __init__(self):
        self.tag = None
        self.content = ""
        self.childs = []
        self.attributes = {}

    def addchild(self , child):
        self.childs.append(child)

    def __getitem__(self , key):
        return self.childs[key]
    
    def __setitem__(self , key , value):
        self.childs[key] = value


def extract_datas(string):

    if(string.find(" ") != -1):
        
        balise_type = string[0:string.find(" ")]
        index = string.find(" ")

        attributes = {}

        while(string.find("="  , index , len(string)) != -1):

            index += 1

            key = string[index:string.find("=" , index , len(string))]

            guillemet = string.find('"' , index , len(string))
            apostrophe = string.find("'" , index , len(string))

            if ((apostrophe == -1) or ((guillemet != -1) and (guillemet < apostrophe))):
                value = string[guillemet+1:string.find('"' , string.find('"' , index , len(string))+1 , len(string))]

                index = string.find('"' , guillemet+1 , len(string))
            else:
                value = string[apostrophe+1:string.find("'" , string.find("'" , index , len(string))+1 , len(string))]

                index = string.find("'" , apostrophe+1 , len(string))

            attributes[key.strip()] = value
        
        return balise_type , attributes
    else:
        return string , {}

string = ""

with open("this.xml" , newline="",mode="r",encoding="utf-8") as reader:

    while (a := reader.readline()):
        l = a.strip("\n")
        l = l.strip("\r")
        l = l.strip()
        string += l
    
    string = string[string.find(">")+1:]
    string = string.strip()

parts = []
index = 0
while(string.find("<" , index , len(string)) != -1):
    if index != 0:
        content = "<"+string[index:string.find("<" , index , len(string))]+">"
        parts.append(content)
    part = string[string.find("<" , index , len(string))+1:string.find(">" , index , len(string))]
    index = string.find(">" , index , len(string))+1
    parts.append(part)

print(parts)

tree = None

pile = Stack(100)
for part in parts:
    if "<" not in part and ">" not in part:
        if pile.is_empty():
            tree = Tree()
            balise , attributes = extract_datas(part)
            tree.tag = balise
            tree.attributes = attributes
            pile.stack_element(tree)
        else:
            if "/" in part:
                pile.unstack_element()
                continue
            
            tree = pile.unstack_element()
            child = Tree()
            balise , attributes = extract_datas(part)
            child.tag = balise
            child.attributes = attributes
            tree.addchild(child)
            pile.stack_element(tree)
            pile.stack_element(child)
    else:
        element = pile.unstack_element()
        element.content += part[1:-1]
        pile.stack_element(element)

