import pygame
import time

from Teapot import Teapot

teapot = Teapot()
teapot.toggle() #we are running 'spout backwards' for this challenge

pygame.init()
pygame.display.set_mode([50,50])

motoring=False
startspeed = 30 # try runing at X% speed
integral = 0.0
last_proportional = 0.0

Kp = 0.05
Ki = 0.00001
#Kd = 1.5
Kd = 0.0

#motorL = startspeed
#motorR = startspeed

running = True
while running:
	if motoring:
		L = teapot.sensorL
		R = teapot.sensorR

		proportional = L-R
		derivative = proportional - last_proportional
		integral += proportional
		last_proportional = proportional

		print("p %f, i %f, d %f"%(proportional, integral, derivative))
		print("kp %f, ki %f, kd %f"%(proportional*Kp, integral*Ki, derivative*Kd))
		difference = int(proportional*Kp + integral*Ki + derivative*Kd)
		print('difference is %f'%difference)

#restrict motor speed to +- 5 - maybe we can go larger later?
		if difference < -5:
			difference = -5
		if difference > 5:
			difference = 5
#		difference = max(-10, min(difference, 10))
		print('clamped difference is %f'%difference)

		motorL = startspeed-difference
		motorR = startspeed+difference

		print('diff %d motorL %d, motorR %d'%(difference, motorL, motorR))
		teapot.pwm_brushed(Teapot.MOTORB, motorL)
		teapot.pwm_brushed(Teapot.MOTORC, motorR)
		time.sleep(0.1) # stops the IOError?

	events = pygame.event.get()
	for event in events:
		if event.type == pygame.QUIT:
			pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_s:
				if motoring:
					motoring=False
					teapot.stop()
				else:
					motoring = True
					integral = 0.0
					last_proportional = 0.0
#					motorL = startspeed
#					motorR = startspeed
					teapot.forwards()
			if event.key == pygame.K_r:
				integral = 0.0
				last_proportional = 0.0
#				motorL = startspeed
#				motorR = startspeed
			elif event.key == pygame.K_q:
				teapot.stop()
				print('quit')
				running = False
				motoring = False
pygame.quit()
