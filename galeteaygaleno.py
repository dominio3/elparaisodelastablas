#! /usr/bin/python
# -*- coding: utf-8 -*-


import pygame
import sys
import os
import time
import random 
from pygame.locals import *


#Tablas
tablas=[["2x1=2","B"],["2x2=4","B"],["2x3=6","B"],["2x4=8","B"],["2x5=10","B"],["2x6=12","B"],["2x7=14","B"],["2x8=16","B"],["2x9=18","B"],["2x10=20","B"],
["3x1=3","B"],["3x2=6","B"],["3x3=9","B"],["3x4=12","B"],["3x5=15","B"],["3x6=18","B"],["3x7=21","B"],["3x8=24","B"],["3x9=27","B"],["3x10=30","B"],
["4x1=4","B"],["4x2=8","B"],["4x3=12","B"],["4x4=16","B"],["4x5=20","B"],["4x6=24","B"],["4x7=28","B"],["4x8=32","B"],["4x9=36","B"],["4x10=40","B"],
["5x1=5","B"],["5x2=10","B"],["5x3=15","B"],["5x4=20","B"],["5x5=25","B"],["5x6=30","B"],["5x7=35","B"],["5x8=40","B"],["5x9=45","B"],["5x10=50","B"],
["6x1=6","B"],["6x2=12","B"],["6x3=18","B"],["6x4=24","B"],["6x5=30","B"],["6x6=36","B"],["6x7=42","B"],["6x8=48","B"],["6x9=54","B"],["6x10=60","B"],
["7x1=7","B"],["7x2=14","B"],["7x3=21","B"],["7x4=28","B"],["7x5=35","B"],["7x6=42","B"],["7x7=49","B"],["7x8=56","B"],["7x9=63","B"],["7x10=70","B"],
["8x1=8","B"],["8x2=16","B"],["8x3=24","B"],["8x4=32","B"],["8x5=40","B"],["8x6=48","B"],["8x7=56","B"],["8x8=64","B"],["8x9=72","B"],["8x10=80","B"],
["9x1=9","B"],["9x2=18","B"],["9x3=27","B"],["9x4=36","B"],["9x5=45","B"],["9x6=54","B"],["9x7=63","B"],["9x8=72","B"],["9x9=81","B"],["9x10=90","B"],
["10x1=10","B"],["10x2=20","B"],["10x3=30","B"],["10x4=40","B"],["10x5=50","B"],["10x6=60","B"],["10x7=70","B"],["10x8=80","B"],["10x9=90","B"],["10x10=100","B"],
["2x1=8","M"],["2x2=2","M"],["2x3=8","M"],["2x4=10","M"],["2x5=12","M"],["2x6=15","M"],["2x7=18","M"],["2x8=19","M"],["2x9=20","M"],["2x10=22","M"],
["3x1=6","M"],["3x2=5","M"],["3x3=5","M"],["3x4=2","M"],["3x5=18","M"],["3x6=15","M"],["3x7=24","M"],["3x8=48","M"],["3x9=50","M"],["3x10=55","M"],
["4x1=8","M"],["4x2=10","M"],["4x3=16","M"],["4x4=18","M"],["4x5=25","M"],["4x6=29","M"],["4x7=40","M"],["4x8=52","M"],["4x9=60","M"],["4x10=50","M"],
["5x1=1","M"],["5x2=15","M"],["5x3=10","M"],["5x4=25","M"],["5x5=35","M"],["5x6=33","M"],["5x7=88","M"],["5x8=58","M"],["5x9=2","M"],["5x10=28","M"],
["6x1=8","M"],["6x2=18","M"],["6x3=24","M"],["6x4=30","M"],["6x5=36","M"],["6x6=35","M"],["6x7=40","M"],["6x8=45","M"],["6x9=50","M"],["6x10=56","M"],
["7x1=14","M"],["7x2=21","M"],["7x3=28","M"],["7x4=35","M"],["7x5=42","M"],["7x6=35","M"],["7x7=40","M"],["7x8=45","M"],["7x9=50","M"],["7x10=56","M"],
["8x1=16","M"],["8x2=24","M"],["8x3=32","M"],["8x4=40","M"],["8x5=18","M"],["8x6=35","M"],["8x7=40","M"],["8x8=45","M"],["8x9=50","M"],["8x10=88","M"],
["9x1=18","M"],["9x2=27","M"],["9x3=36","M"],["9x4=45","M"],["9x5=54","M"],["9x6=60","M"],["9x7=80","M"],["9x8=45","M"],["9x9=50","M"],["9x10=80","M"],
["10x1=12","M"],["10x2=30","M"],["10x3=40","M"],["10x4=50","M"],["10x5=60","M"],["10x6=70","M"],["10x7=80","M"],["10x8=9","M"],["10x9=58","M"],["10x10=101","M"]]

pygame.init()

def tablasrandom(lista):
	cuenta=random.choice(lista)
	return cuenta

def pantallaprincipal():
#~ Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Paraiso de Tablas con Galeno y Galatea")
	fondo=pygame.image.load(os.path.join('imagenes','pantallabienvenida.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#~ pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','sonidodefondo.wav'))
	pygame.mixer.music.play(20)
#~ Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
	texto = fuente.render(u'Presioná Enter para continuar', True, pygame.Color(0,0,0))
	pantalla.blit(texto, (630,35))
	fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),25)
	texto = fuente.render(u'Presioná Escape para salir', True, pygame.Color(0,0,0))
	pantalla.blit(texto, (0,10))
	fuente = pygame.font.Font(os.path.join('tipografias','segoepr.ttf'),19)
	firma = fuente.render(u'Creadores: Jorge Gamez y Nadia Maguicha (U.N.A.J).', True, pygame.Color(0,0,0))
	pantalla.blit(firma, (400,675))
	pygame.display.flip()
#~ Efectos de sonido
 
def pantallaelijojugador():
#~ Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Elije un Jugador")
	fondo=pygame.image.load(os.path.join('imagenes','jugadores.png'))
	pantalla.blit(fondo,(0,0))
#~ pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','sonidodejugadores.wav'))
	pygame.mixer.music.play(3)
#~ Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','segoepr.ttf'),18)
	texto = fuente.render(u'elige con las teclas', True, pygame.Color(0,0,0))
	pantalla.blit(texto, (370,561))
	pygame.display.flip()
	
	
	
def pantallainstruccionesgaleno():
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Instrucciones")
	fondo=pygame.image.load(os.path.join('imagenes','instruccionesgaleno.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','sonidodefondo.wav'))
	pygame.mixer.music.play(3)
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','segoepr.ttf'),30)
	texto = fuente.render(u'Presioná Enter para continuar...', True, pygame.Color(0,0,0))
	pantalla.blit(texto, (430,645))
	pygame.display.flip()



def pantallainstruccionesgalatea():
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Instrucciones")
	fondo=pygame.image.load(os.path.join('imagenes','instruccionesgala.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','sonidodefondo.wav'))
	pygame.mixer.music.play(3)
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','segoepr.ttf'),30)
	texto = fuente.render(u'Presioná Enter para continuar...', True, pygame.Color(0,0,0))
	pantalla.blit(texto, (430,645))
	pygame.display.flip()

def ganastegaleno(puntaje):
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Lo lograste eres un genio!!!")
	fondo=pygame.image.load(os.path.join('imagenes','ganastegaleno.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','ganaste.wav'))
	pygame.mixer.music.play()
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
	textonivel = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
	pantalla.blit(textonivel, (750,630))
	pygame.display.flip()

def perdistegaleno(puntaje):
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption(u'Volve a intentarlo')
	fondo=pygame.image.load(os.path.join('imagenes','perdistegaleno.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','perdiste.wav'))
	pygame.mixer.music.play()
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','segoepr.ttf'),20)
	textonivel = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
	pantalla.blit(textonivel, (750,630))
	pygame.display.flip()

	
	
def ganastegalatea(puntaje):
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption("Lo lograste eres una genia!!!")
	fondo=pygame.image.load(os.path.join('imagenes','ganastegalatea.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','ganaste.wav'))
	pygame.mixer.music.play()
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
	textonivel = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
	pantalla.blit(textonivel, (750,630))
	pygame.display.flip()
	


def perdistegalatea(puntaje):
#Creo pantalla 
	pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
	pygame.display.set_caption(u'Volve a intentarlo')
	fondo=pygame.image.load(os.path.join('imagenes','perdistegalatea.png'))
	pantalla.blit(fondo,(0,0))
	base=pantalla.copy()
#pongo sonido
	pygame.mixer.music.set_volume(0.9)
	pygame.mixer.music.load(os.path.join('sonidos','perdiste.wav'))
	pygame.mixer.music.play()
#Escribo texto
	fuente = pygame.font.Font(os.path.join('tipografias', 'segoepr.ttf'),20)
	textonivel = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
	pantalla.blit(textonivel, (750,630))
	pygame.display.flip()

def reloj(pantalla):
	for bucle in range[8,7,6,5,4,3,2,1,0]:
		rolex=pygame.image.load(os.path.join('imagenes','reloj',bucle,'.png'))
		pantalla.blit(rolex,(0,0))
		base=pantalla.copy()


nivel=1	
puntaje=0
jugador=""
comienza=False
def juego():
	while comienza==False:
		for event in pygame.event.get():
			if event.type == QUIT:
				salir=True
				pygame.quit
				sys.exit()
		
		pantallaprincipal()
		
		salir=False
		while salir==False:
			
			for event in pygame.event.get():
				if event.type == QUIT:
					salir=True
					pygame.quit
					sys.exit()
		        else:
		            if event.type ==  KEYDOWN:
						if event.key == K_ESCAPE:
							salir=True
							pygame.quit
							sys.exit()
						elif event.key ==13:
							pantallaelijojugador()
							salir=True
		salir=False	
							
		while salir==False:
			
			for event in pygame.event.get():
				if event.type == QUIT:
					salir=True
					pygame.quit()
					sys.exit()
		        else:
					if event.type ==  KEYDOWN:
						if event.key ==K_LEFT:
							jugador="Galeno"
							puntaje=0
							pantallainstruccionesgaleno()
							salir=True
						if event.key ==K_RIGHT:
							jugador="Galatea"
							puntaje=0
							pantallainstruccionesgalatea() 	
							salir=True
		                
			pygame.display.update()
		
		salir=False
		vuelta=0
		while salir!=True:
			
			
		
			for event in pygame.event.get():
				
				if event.type == QUIT:
					salir=True
					pygame.quit()
					sys.exit()
		        
				elif event.type ==  KEYDOWN:
					
					if event.key==K_ESCAPE:
						salir=True
						pygame.quit()
						sys.exit()
						
					elif event.key == K_b  and criterio=="B":
						puntaje=puntaje+100
					elif event.key == K_m  and criterio=="M":
						puntaje=puntaje+100
					elif event.key == K_b:
						puntaje=puntaje-100
					elif event.key == K_m:
						puntaje=puntaje-100
					
					nivel1=0
					if jugador=="Galeno":
							
							
						cuenta=random.choice(tablas)
						cuentita=cuenta[0]	
						criterio=cuenta[1]
						pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
						pygame.display.set_caption("Date prisa!!!")
						fondo=pygame.image.load(os.path.join('imagenes','galeno.png'))
						pantalla.blit(fondo,(0,0))
						base=pantalla.copy()
						#pongo sonido
						pygame.mixer.music.set_volume(0.9)
						pygame.mixer.music.load(os.path.join('sonidos','sonidodejuego.wav'))
						pygame.mixer.music.play(30)
						#Escribo texto
						fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
						textonivel = fuente.render(str(nivel), True, pygame.Color(0,0,0))
						pantalla.blit(textonivel, (800,400))
						pygame.display.flip()
						fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
						textopuntaje = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
						pantalla.blit(textopuntaje, (800,540))
						pygame.display.flip()
						fuente = pygame.font.Font(os.path.join('tipografias','comic.ttf'),50)
						textotablas = fuente.render(str(cuentita), True, pygame.Color(255,255,255))
						pantalla.blit(textotablas, (200,240))
						pygame.display.flip()
						if nivel1==0:
							reloj=pygame.image.load(os.path.join('imagenes','reloj8.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==1:
							reloj=pygame.image.load(os.path.join('imagenes','reloj7.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==2:
							reloj=pygame.image.load(os.path.join('imagenes','reloj6.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==3:
							reloj=pygame.image.load(os.path.join('imagenes','reloj5.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==4:
							reloj=pygame.image.load(os.path.join('imagenes','reloj4.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==5:
							reloj=pygame.image.load(os.path.join('imagenes','reloj3.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==6:
							reloj=pygame.image.load(os.path.join('imagenes','reloj2.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==7:
							reloj=pygame.image.load(os.path.join('imagenes','reloj1.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						else:
							reloj=pygame.image.load(os.path.join('imagenes','reloj0.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						pygame.display.flip()
						time.sleep(1)
					
	
					nivel1=0
					if jugador=="Galatea":
						
						cuenta=random.choice(tablas)
						cuentita=cuenta[0]	
						criterio=cuenta[1]
						pantalla=pygame.display.set_mode((921,716),FULLSCREEN,32)
						pygame.display.set_caption("Date prisa!!!")
						fondo=pygame.image.load(os.path.join('imagenes','galatea.png'))
						pantalla.blit(fondo,(0,0))
						base=pantalla.copy()
						#pongo sonido
						pygame.mixer.music.set_volume(0.9)
						pygame.mixer.music.load(os.path.join('sonidos','sonidodejuego.wav'))
						pygame.mixer.music.play(30)
						#Escribo texto
						fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
						textonivel = fuente.render(str(nivel), True, pygame.Color(0,0,0))
						pantalla.blit(textonivel, (800,400))
						pygame.display.flip()
						fuente = pygame.font.Font(os.path.join('tipografias','Walt Disney Script.ttf'),30)
						textopuntaje = fuente.render(str(puntaje), True, pygame.Color(0,0,0))
						pantalla.blit(textopuntaje, (800,540))
						pygame.display.flip()
						fuente = pygame.font.Font(os.path.join('tipografias','comic.ttf'),50)
						textotablas = fuente.render(str(cuentita), True, pygame.Color(255,255,255))
						pantalla.blit(textotablas, (200,240))
						pygame.display.flip()
					for nivel1 in range(8):	
						if nivel1==0:
							reloj=pygame.image.load(os.path.join('imagenes','reloj8.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==1:
							reloj=pygame.image.load(os.path.join('imagenes','reloj7.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==2:
							reloj=pygame.image.load(os.path.join('imagenes','reloj6.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==3:
							reloj=pygame.image.load(os.path.join('imagenes','reloj5.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==4:
							reloj=pygame.image.load(os.path.join('imagenes','reloj4.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==5:
							reloj=pygame.image.load(os.path.join('imagenes','reloj3.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==6:
							reloj=pygame.image.load(os.path.join('imagenes','reloj2.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						elif nivel1==7:
							reloj=pygame.image.load(os.path.join('imagenes','reloj1.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
						else:
							reloj=pygame.image.load(os.path.join('imagenes','reloj0.png'))
							pantalla.blit(reloj,(30,30))
							base=pantalla.copy()
							
						pygame.display.flip()
					time.sleep(1)
					
						
					if puntaje<=-400 and jugador=="Galeno":
						perdistegaleno(puntaje)
						salir=True
						vuelta=10
					elif puntaje>=400 and jugador=="Galeno":
						ganastegaleno(puntaje)
						salir=True
						
					elif puntaje<=-400 and jugador=="Galatea":
						perdistegalatea(puntaje)
						salir=True
						vuelta=10
					elif puntaje>=400 and jugador=="Galatea":
						ganastegalatea(puntaje)
						salir=True
							
							
							
					time.sleep(4)
		puntaje=0
		
							
		pygame.display.update()


juego()
