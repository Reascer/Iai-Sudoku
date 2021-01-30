class elementManager:
    def __init__(self):
        self.elements = []

    def addElement(self,element):
        self.elements.append(element)

    def renderElements(self,screen,index=None):
        for element in self.elements:
            element.render(screen)
        if index is not None:
            self.elements[index].render(screen)

    def EventElements(self,event):
        for element in self.elements:
            action = element.eventElmt(event)
            if not action == None:
                return action

    



