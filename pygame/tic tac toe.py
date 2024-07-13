#портфолио
import pygame
import random
def vin (a):
  if krest[0][0]==krest[1][1]==krest[2][2]==a:
    return True
  if krest[2][0]==krest[1][1]==krest[0][2]==a:
    return True
  for i in range(3):
    if krest[0][i]==krest[1][i]==krest[2][i]==a:
      return True
  for i in krest:
    if i.count(a)==3:
      return True
  return False


def dru():
  for i in range(3):
    for g in range(3):
      if krest[i][g]=="x":
        pygame.draw.line(win,green,(g*100+5,i*100+5),(g*100+95,i*100+95),2)
        pygame.draw.line(win,green,(g*100+95,i*100+5),(g*100+5,i*100+95),2)
      if krest[i][g]=="0":
        pygame.draw.circle(win,green,(g*100+50,i*100+50),45,2)
win=pygame.display.set_mode((300,300))
pygame.display.set_caption("крестеки нолики")
pygame.init()
white = (255,255,255)
green = (86, 201, 197)
black = (0,0,0)
clock = pygame.time.Clock()
krest=[[" "," "," "],
      [" "," "," "],
      [" "," "," "] ]
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()
    if event.type==pygame.MOUSEBUTTONDOWN:
      muse=pygame.mouse.get_pos()
      if krest[muse[1]//100][muse[0]//100]==" ":
        krest[muse[1]//100][muse[0]//100]="x"
        x=random.randint(0,2)
        y=random.randint(0,2)
        while krest[x][y]!=" ":
           x=random.randint(0,2)
           y=random.randint(0,2)
        else:
           krest[x][y]="0"
  b=vin("x")
  l=vin("0")
  if b == True :
    pygame.display.set_caption("ты победил")
  if l == True:
    pygame.display.set_caption("ты проиграл")
  win.fill(white)
  pygame.draw.line(win,black,(100,0),(100,300),2)
  pygame.draw.line(win,black,(200,0),(200,300),2)
  pygame.draw.line(win,black,(0,100),(300,100),2)
  pygame.draw.line(win,black,(0,200),(300,200),2)
  dru()

  pygame.display.flip()
  clock.tick(30)