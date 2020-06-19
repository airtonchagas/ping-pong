from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.core.window import Window


# Definição do
class Pong(Widget):

    bola = ObjectProperty(None)


    raquete_1 = ObjectProperty(None)
    raquete_2 = ObjectProperty(None)

    def __init__(self, screen_manager=None):
        super(Pong, self).__init__()
        self.screen_manager = screen_manager
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)

    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None


    def servico(self, vel=(4, 0)):


        self.bola.center = self.center


        self.bola.velocidade = vel


    def atualiza(self, dt):



        self.bola.movimenta()


        self.raquete_1.rebate_bola(self.bola)
        self.raquete_2.rebate_bola(self.bola)


        if (self.bola.y < 0) or (self.bola.top > self.height):
            self.bola.velocidade_y *= -1


        if self.bola.x < self.x:

            self.raquete_2.placar += 1

            if self.raquete_2.placar >= 3:
                self.servico(vel=(0, 0))
                self.raquete_1.placar = 0
                self.raquete_2.placar = 0
                self.screen_manager.current = "vencedor_2"

                return


            self.servico(vel=(4, 0))

        if self.bola.x > self.width:

            self.raquete_1.placar += 1

            if self.raquete_1.placar >= 3:
                self.servico(vel=(0, 0))
                self.raquete_1.placar = 0
                self.raquete_2.placar = 0
                self.screen_manager.current = "vencedor_1"

                return


            self.servico(vel=(-4, 0))

    # # Captura o evento on_touch_move (arrastar de dedo na tela)
    # def on_touch_move(self, touch):
    #     # Verifica se toque foi do lado esquerdo da tela
    #     if touch.x < self.width / 2:
    #         # Atualiza altura da raquete esquerda
    #         self.raquete_1.center_y = touch.y

    #     # Verifica se toque foi do lado direito da tela
    #     if touch.x > self.width - self.width / 2:
    #         # Atualiza altura da raquete direita
    #         self.raquete_2.center_y = touch.y

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if keycode[1] == 'w':
            if(self.raquete_1.center_y <= 617.5 ):
                self.raquete_1.center_y += 10

        elif keycode[1] == 's':
            if(self.raquete_1.center_y >= 97.5 ):
                self.raquete_1.center_y -= 10

        elif keycode[1] == 'up':
            if(self.raquete_2.center_y <= 617.5 ):
                self.raquete_2.center_y += 10

        elif keycode[1] == 'down':
            if(self.raquete_2.center_y >= 97.5 ):
                self.raquete_2.center_y -= 10

        return True


    def remove_btn(self, btn):


        self.remove_widget(btn)

    def comeca_jogo(self):


        self.servico()


        Clock.schedule_interval(self.atualiza, 1.0/120.0)

    def reinicia_jogo(self):

        self.servico(vel=(4,0))

        self.raquete_1.placar = 0
        self.raquete_2.placar = 0
