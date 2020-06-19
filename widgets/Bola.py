from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.widget import Widget
from kivy.vector import Vector

class Bola(Widget):


    velocidade_x = NumericProperty(0)
    velocidade_y = NumericProperty(0)


    velocidade = ReferenceListProperty(velocidade_x, velocidade_y)


    def movimenta(self):
        self.pos = Vector(*self.velocidade) + self.pos
