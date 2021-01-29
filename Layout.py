# Layout.py

class Layout:
    def __init__(self):        
        self.listElmtTab = []
        self.listElmtManager = []

    def event(self, event):
        for elmt in self.listElmtManager:
            action = elmt.EventElements(event)
            if not action == None:
                return action
    
    def render(self, screen):
        for elmnt in self.listElmtManager:
            elmnt.renderElements(screen)

    def update(self):
        pass

    def addElmtManager(self, elmtManager):
        self.listElmtManager.append(elmtManager)       

    def addElmt(self, element):
        self.listElmtTab.append(element)
        
    