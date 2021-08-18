# Nilupul CEO
#    |__ Chinmay CTO
#       |__ Vishwa Infra Head
#          |__ Dhaval Cloud Manager
#          |__ Abhijit App Manager
#       |__ Aamir Application Head
#    |__ Gels HR Head
#       |__ Peter Recurit Manager
#       |__ Waqas Policy Manager

class Nodes:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self, child):
        child.parent = self
        self.children.append(child)

    def printer(self):
        spaces = " " * self.leveler() * 3
        prefix = spaces + "|__ " if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.printer()

    def leveler(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level


def tracer():
    root = Nodes("Nilupul CEO")
    cto = Nodes("Chinmay CTO")
    infraHead = Nodes("Vishwa Infra Head")
    appHead = Nodes("Aamir Application Head")
    cloudManager = Nodes("Dhaval Cloud Manager")
    appManager = Nodes("Abhijit App Manager")

    hrhead = Nodes("Gels HR Head")
    recManager = Nodes("Peter Recurit Manager")
    policyManager = Nodes("Waqas Policy Manager")

    root.addChild(cto)
    cto.addChild(infraHead)
    infraHead.addChild(cloudManager)
    infraHead.addChild(appManager)
    cto.addChild(appHead)

    root.addChild(hrhead)
    hrhead.addChild(recManager)
    hrhead.addChild(policyManager)
    return root


if __name__ == '__main__':
    rooter = tracer()
    rooter.printer()
