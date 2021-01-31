
#====================== Class ElementManager - Conteneur d'une liste d'éléments ===========================#

class elementManager:
    def __init__(self):
        self.elements = []

#====================== Ajout d'un élément dans la liste d'éléments de l'objet ===========================#

    def addElement(self,element):
        self.elements.append(element)

#====================== Affichage des éléments ===========================#

    def renderElements(self,screen,index=None):
        for element in self.elements:
            element.render(screen)
        if index is not None:
            self.elements[index].render(screen)

#====================== Event sur un élément ===========================#

    def EventElements(self,event):
        for element in self.elements:
            action = element.event(event)
            if not action == None:
                return action
