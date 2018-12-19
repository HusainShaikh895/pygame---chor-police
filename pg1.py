import pygame
#My first graphical game in python- Two players play simultaneously, red circle tries to catch green one
#If the green circle gets caught red wins
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Baskerville', 30)

#for writing to the game
window=pygame.display.set_mode((500, 500))
#setting window size
pygame.display.set_caption("Chor-Police")
#Title of the window
x=50
y=50
x1=410
y1=410
rad=12
velb=10
velg=10
#velocity of each circle
cop_score=0


run=True
while run:
	#pygame.time.delay(10)

	for event in pygame.event.get():
		if event.type== pygame.QUIT:
			run=False

		keys= pygame.key.get_pressed()
# For player red
		if keys[pygame.K_LEFT] and (x-velb)>0:
			x=x-velb
		if keys[pygame.K_RIGHT] and (x+velb)<500:
			x=x+velb
		if keys[pygame.K_UP] and (y-velb)>0:
			y=y-velb
		if keys[pygame.K_DOWN] and (y+velb)<500:
			y=y+velb
# For player green
		if keys[pygame.K_a] and (x1-velg)>0:
			x1-=velg
		if keys[pygame.K_d] and (x1+velg)<500:
			x1+=velg
		if keys[pygame.K_w] and (y1-velg)>0:
			y1-=velg
		if keys[pygame.K_s] and (y1+velg)<500:
			y1+=velg


		if((x==x1 and y==y1)):
			cop_score+=1
			#Below lines are not doing anything----
			pygame.display.update()
			window.fill((255,0,0))
			#wanted to show red screen 
			pygame.display.update()
			#------------
			print("Green got caught!!! Red won")
			print("Score : {}".format(cop_score))
			pygame.time.delay(2000)
			x=50
			y=50
			x1=410
			y1=410
		#initiliasing 
		window.fill((255,255,255))
		#whilte window fill
	pygame.draw.circle(window,(255,0,0),(x,y),rad,0)
	pygame.draw.circle(window,(0,255,0),(x1,y1),rad,0)
	pygame.display.update()
	


pygame.quit()
