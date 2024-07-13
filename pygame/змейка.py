#портфолио
import pygame
import random 
# пораметы окна и змейки
shir=600
vist=600
rasmer=30
x=300
y=300
zmeika=[(x,y)]
rost=1
dvix=0
dviy=0
red = (200,0,0)
win=pygame.display.set_mode((600,600))

apl2=(pygame.draw.circle(win,red, (100, 100), 50))
dvs={"up":True, "down":True, "left":True, "right":True}
apl=(random.randrange(0,shir,rasmer),random.randrange(0,vist,rasmer))

pygame.display.set_caption("змейка")
pygame.init()
white = (255,255,255)
green = (86, 201, 197)

black = (0,0,0)
clock = pygame.time.Clock()
# кводрат змейки
zmeika2=pygame.Rect(x,y,rasmer,rasmer)
# нажатие клавишь
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()
    elif  event.type==pygame.KEYDOWN:
      if event.key==pygame.K_LEFT and dvs["left"]:
        dvix=-1
        dviy=0
        dvs={"up":True, "down":True, "left":True, "right":False}
      elif event.key==pygame.K_UP and dvs["up"]:
        dvix=0
        dviy=-1
        dvs={"up":True, "down":False, "left":True, "right":True}
      elif event.key==pygame.K_RIGHT and dvs ["right"]:
        dvix=1
        dviy=0
        dvs={"up":True, "down":True, "left":False, "right":True}
      elif event.key==pygame.K_DOWN and dvs ["down"]:
        dvix=0
        dviy=1
        dvs={"up":False, "down":True, "left":True, "right":True}

  x+=dvix*30
  y+=dviy*30
  zmeika.insert(0,(x,y))
  if len (zmeika)>rost:
    zmeika.pop()
  if (x<0 or x>vist-rasmer or y<0 or y >shir - rasmer)or len(zmeika)!=len(set(zmeika)):
    dvix,dviy=0,0
    x=300
    y=300
    zmeika=[(x,y)]
    rost=1
  if zmeika[0]==apl:
    apl=(random.randrange(0,shir,rasmer),random.randrange(0,vist,rasmer))
    rost+=1
    # отрисовка змейки
  for i in zmeika:
   
    if i ==zmeika[0]:
      pygame.draw.rect(win,green,(i[0],i[1],rasmer-2,rasmer-2))     
    else :
      pygame.draw.rect(win,black,(i[0],i[1],rasmer-2,rasmer-2))     
  while apl in zmeika:
    apl=(random.randrange(0,shir,rasmer),random.randrange(0,vist,rasmer))
  pygame.draw.ellipse(win,red,(apl[0],apl[1],rasmer,rasmer)) 
     
   
  # if zmeika2.right < 0 :
  #  zmeika2.left = 580
  # if zmeika2.left > 600 :
  #  zmeika2.right = 0
  # if zmeika2.bottom  < 0 :
  #   zmeika2.top =600
  # if zmeika2.top > 600:
  #   zmeika2.bottom=0
  
  # pygame.draw.rect(win,black,zmeika2)     
  
  

  pygame.display.update()
  win.fill(white)
  clock.tick(7)

  # Офрмить внешний вид - подобрать какие-нибудь новые цвета
  # Сделать яблоко кругом или элипсом 
  # дополнительно - нарисовать границы экрана 
  #https://younglinux.info/pygame/draw