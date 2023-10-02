
import Shapes2D  

class CartesianBoard:
    def __init__(self):
        self.shapes = {}

    def insertShape(self, shape):
        self.shapes[shape.getType() + str(shape.getNumber())] = shape

    def removeShape(self, shape):
        del self.shapes[shape.getType() + str(shape.getNumber())]

    def showShapes(self):
        print('\nEste plano cartesiano possui as seguintes formas:\n')
        for shape in self.shapes.keys():
            print(shape)

    def printDetails(self):
        for key in self.shapes.keys():
            if isinstance(self.shapes[key], Shapes2D.Ponto) or isinstance(self.shapes[key], Shapes2D.Circulo):
                self.shapes[key].printCoord()
            if not isinstance(self.shapes[key], Shapes2D.Ponto):
                self.shapes[key].area()
                self.shapes[key].perimetro()
                if not isinstance(self.shapes[key], Shapes2D.Circulo):
                    self.shapes[key].diagonal()

    def getShape(self, key):
        return self.shapes[key]
