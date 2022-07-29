# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

from pygame import mixer  # é necessário antes instalar o package pygame
mixer.init()
mixer.music.load('ex021music.mp3')
mixer.music.play()
input('Agora você escuta? ')
