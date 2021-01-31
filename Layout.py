
#====================== Class Layout - Conteneur type d'une page de l'application ===========================#

class Layout:
    def __init__(self):        
        self.listElmtTab = []
        self.listElmtManager = []

#====================== Event dans un layout ===========================#

    def event(self, event):
        for elmt in self.listElmtManager:
            action = elmt.EventElements(event)
            if not action == None:
                return action
    
#====================== Affichage des éléments contenu dans le Layout ===========================#

    def render(self, screen):
        for elmnt in self.listElmtManager:
            elmnt.renderElements(screen)

#====================== Ajout d'un objet ElementManager à la liste d'ElementManager de l'objet courant ===========================#

    def addElmtManager(self, elmtManager):
        self.listElmtManager.append(elmtManager)       

#====================== Ajout d'un objet Element à la liste d'Element de l'objet courant ===========================#

    def addElmt(self, element):
        self.listElmtTab.append(element)
        
    