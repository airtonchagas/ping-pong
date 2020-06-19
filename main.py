#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Imports
from kivy.app        import App
from kivy.uix.widget import Widget
from kivy.vector     import Vector
from kivy.lang       import Builder
from kivy.config     import Config
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from widgets         import Pong, Raquete, Bola
from telas           import *
from kivy.uix.screenmanager import ScreenManager, Screen

Config.read("config.ini")
Config.set('graphics', 'window_state', 'maximized')

screen_manager = ScreenManager()

class PongApp(App):

    def build(self):


        sound = SoundLoader.load('audio/bg-music.mp3')


        if sound:
            sound.play()


        pong = Pong(screen_manager=screen_manager)


        tela_jogo = TelaJogo(name="jogo")


        tela_jogo.add_widget(pong)


        screen_manager.add_widget(TelaMenu(name='menu'))
        screen_manager.add_widget(tela_jogo)
        screen_manager.add_widget(TelaVencedor1(name='vencedor_1'))
        screen_manager.add_widget(TelaVencedor2(name='vencedor_2'))

        return screen_manager

if __name__ == '__main__':
    PongApp().run()
