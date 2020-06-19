from kivy.properties import NumericProperty
from kivy.uix.widget import Widget
from kivy.vector     import Vector

class Raquete(Widget):

    placar = NumericProperty(0)

    def rebate_bola(self, bola):

        
        if (self.collide_widget(bola)):


            vx, vy = bola.velocidade


            offset_raquete = (bola.center_y - self.center_y) / (self.height / 2)


            inv_vel = Vector(-1 * vx, vy)

            
            if((inv_vel[0] >= -7) or (inv_vel[1] >= -7)):

                vel = inv_vel * 1.1
            else:
                vel = inv_vel

            bola.velocidade = vel.x, vel.y + (offset_raquete * 2)
            print(bola.velocidade)
