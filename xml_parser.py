
class Stack :

    def __init__(self, size) :
        self.size = size
        self.contenu = []

    def empiler(self, element) :
        if self.is_full() :
            print("Impossible, the stack is full !")
        else :
            self.contenu.append(element)

    def depiler(self) :
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
        self.value = None
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
            value = string[string.find('"' , index , len(string))+1:string.find('"' , string.find('"' , index , len(string))+1 , len(string))]

            index = string.find('"' , string.find('"' , index , len(string))+1 , len(string))

            attributes[key] = value
        
        return balise_type , attributes
    else:
        return string , {}

string = ""

with open("this.xml" , newline="",mode="r") as reader:

    while (a := reader.readline()):
        l = a.strip("\n")
        l = l.strip("\r")
        l = l.strip()
        string += l
    
    string = string[string.find(">")+1:]
    string = string.strip()

parts = []
index = 0
while((part := string[string.find("<" , index , len(string))+1:string.find(">" , index , len(string))]) 
    and string.find("<" , index , len(string)) != -1):
    index = string.find(">" , index , len(string))+1
    parts.append(part)

print(parts)

tree = None

pile = Stack(100)
for part in parts:
    if pile.is_empty():
        tree = Tree()
        balise , attributes = extract_datas(part)
        tree.value = balise
        tree.attributes = attributes
        pile.empiler(tree)
    else:
        if "/" in part:
            pile.depiler()
            continue
        
        tree = pile.depiler()
        child = Tree()
        balise , attributes = extract_datas(part)
        child.value = balise
        child.attributes = attributes
        tree.addchild(child)
        pile.empiler(tree)
        pile.empiler(child)

print(tree.attributes)
# print(parts[0][0:5:-1])

# print(parts)
# print(string)