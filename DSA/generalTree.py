# Electricity
#    |__ TV
#       |__ Samsung
#       |__ Apple
#       |__ Panasonic
#    |__ Mobile
#       |__ Nokia
#       |__ Viv
#       |__ Oppo

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def childItem(self, child):
        child.parent = self
        self.children.append(child)

    def leveler(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def printer(self):
        spaces = ' ' * self.leveler() * 3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for c in self.children:
                c.printer()


def build_protect_tree():
    root = Node("Electricity")
    laptop = Node("TV")
    laptop.childItem(Node("Samsung"))
    laptop.childItem(Node("Apple"))
    laptop.childItem(Node("Panasonic"))


    mobile = Node("Mobile")
    mobile.childItem(Node("Nokia"))
    mobile.childItem(Node("Viv"))
    mobile.childItem(Node("Oppo"))

    root.childItem(laptop)
    root.childItem(mobile)
    #laptop.leveler()
    return root


if __name__ == '__main__':
    rooter = build_protect_tree()
    rooter.printer()
