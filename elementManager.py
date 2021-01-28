import element as elmt

class elementManager:
    def __init__(self):
        self.elements = []

    def addElement(self,pos_x,pos_y,texture=None):
        self.elements.append(elmt.element(pos_x,pos_y,texture))

    def renderElements(self,screen):
        for element in self.elements:
            element.render(screen)

