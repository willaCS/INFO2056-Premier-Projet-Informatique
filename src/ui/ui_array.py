from utils.draw import isInRectangle

class Bouton:
    def __init__(
            self,
            z,
            rect,
            drawArg,
            exec = None,
            execOutside = lambda: None
        ):
        self.z = z
        self.rect = rect
        self.drawArg = drawArg
        self.exec = exec
        self.execOutside = execOutside

    def draw(self):
        r = self.rect if not callable(self.rect) else self.rect()
        self.drawArg(r)
    
    def click(self, pos):
        if self.exec is None:
            self.execOutside()
            return False
        r = self.rect if not callable(self.rect) else self.rect()
        print(r)
        if isInRectangle(pos, r):
            self.exec()
            return True
        else:
            self.execOutside()
            return False
    
    def clickOutside(self, pos):
        r = self.rect if not callable(self.rect) else self.rect()
        if not isInRectangle(pos, r):
            self.execOutside()



class Composant:
    def __init__(self, z, buttons):
        self.z = z
        self.buttons = buttons
        self.hidden = True
    
    def hide(self):
        self.hidden = True
    
    def show(self):
        self.hidden = False

    def draw(self):
        if self.hidden:
            return
        self.buttons.sort(key=lambda b: b.z)
        for button in self.buttons:
            button.draw()
    
    def click(self, pos):
        if self.hidden:
            return False
        self.buttons.sort(key=lambda c: c.z, reverse=True)
        for button in self.buttons:
            if button.click(pos):
                return True
        return False
    
    def clickOutside(self, pos):
        if self.hidden:
            return
        for button in self.buttons:
            button.clickOutside(pos)

class Menu:
    def __init__(self):
        self.composants = []
    
    def add(self, composant):
        self.composants.append(composant)

    def draw(self):
        self.composants.sort(key=lambda c: c.z)
        for composant in self.composants:
            if not composant.hidden:
                composant.draw()
    
    def click(self, pos):
        has_clicked = False
        self.composants.sort(key=lambda c: c.z, reverse=True)
        for composant in self.composants:
            if composant.hidden:
                continue
            if has_clicked:
                composant.clickOutside(pos)
                continue
            if composant.click(pos):
                has_clicked = True
        return has_clicked

menu = Menu()