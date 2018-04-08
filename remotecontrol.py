#seems to require running the gertbot code first?
#import os
#os.environ['SDL_VIDEODRIVER'] = 'dummy'
import time
import pygame

import Teapot

teapot = Teapot.Teapot()

pygame.init()
pygame.display.set_mode([50,50])
#pygame.event.set_grab(True)

print('let us begin')
running = True
while running:
	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				teapot.left()
				print('left')
			elif event.key == pygame.K_RIGHT:
				teapot.right()
				print('right')
			elif event.key == pygame.K_UP:
				teapot.forwards()
				print('up')
			elif event.key == pygame.K_DOWN:
				teapot.backwards()
				print('backwards')
			elif event.key == pygame.K_p:
				print('clockwise')
				teapot.clockwise()
			elif event.key == pygame.K_o:
				print('anticlockwise')
				teapot.anticlockwise()
			elif event.key == pygame.K_u:
				teapot.catcher_up()
			elif event.key == pygame.K_d:
				teapot.catcher_down()
			elif event.key == pygame.K_f:
				teapot.fire()
			elif event.key == pygame.K_r:
				teapot.toggle()
			elif event.key == pygame.K_q:
				teapot.stop()
				print('quit')
				running = False
			elif event.key == pygame.K_1:
				teapot.speed(10)
			elif event.key == pygame.K_2:
				teapot.speed(20)
			elif event.key == pygame.K_3:
				teapot.speed(30)
			elif event.key == pygame.K_4:
				teapot.speed(40)
			elif event.key == pygame.K_5:
				teapot.speed(50)
			elif event.key == pygame.K_6:
				teapot.speed(60)
			elif event.key == pygame.K_7:
				teapot.speed(70)
			elif event.key == pygame.K_8:
				teapot.speed(80)
			elif event.key == pygame.K_9:
				teapot.speed(90)
			elif event.key == pygame.K_0:
				teapot.speed(100)
			else:
				print(event.key)
		elif event.type == pygame.KEYUP:
			teapot.stop()
			print('stop')
pygame.quit()
