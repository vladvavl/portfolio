#портфолио
import pygame
import random       
win=pygame.display.set_mode((700,400))
pygame.display.set_caption("джампер")
pygame.init()
white = (255,255,255)
green = (86, 201, 197)
black = (0,0,0)
blue=(0,255,0)
red=(255,0,0)
font = pygame.font.Font(None, 50)
clock = pygame.time.Clock()
class Obekt:
    def __init__(self, shir, wish, x, y, cvet,speedx,speedy) -> None:
        self.shir = shir  # Ширина объекта
        self.wish = wish  # Высота объекта
        self.x = x  # Координата X объекта на экране
        self.y = y  # Координата Y объекта на экране
        self.cvet = cvet  # Цвет объекта
        self.prim = pygame.Rect(self.x, self.y, self.shir, self.wish)  # Прямоугольник, описывающий объект на экране
        self.speed=[speedx,speedy]#скорость 
    def ris(self):  # Метод для отрисовки прямоугольника
        pygame.draw.rect(win, self.cvet, self.prim)

    def risshar(self):  # Метод для отрисовки эллипса
        pygame.draw.ellipse(win, self.cvet, self.prim)
    def move(self):
       global scor,ohki 
       self.prim=self.prim.move(self.speed)
       if self.prim.left<-50:
          self.prim.right=730
          ohki+=1
    def grav(self):
       if self.prim.bottom>300:
          self.prim.bottom=300
        

scor=30
ohki=0
person=Obekt(90,90,10,210,blue,0,10)
zemla=Obekt(700,100,0,300,green,0,0)
vrag=Obekt(50,50,500,250,red,-10,0)
person.jamp=True
person.jamp_speed=20
person.jamp_nam=0

pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)
while True:
  win.fill(white)
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      pygame.quit()
      exit()
    elif  event.type==pygame.KEYDOWN:
      if event.key==pygame.K_SPACE and person.prim.bottom==300 and not(person.jamp):
        person.jamp=True
        person.jamp_nam=person.jamp_speed

      if event.key==pygame.K_RETURN:
         person.speed=[0,10]
         vrag.speed=[-10,0]
         vrag.prim.x=750

  if person.jamp and person.jamp_nam>0:
      person.prim.y-=person.jamp_speed
      person.jamp_nam-=1
  else:
      person.jamp=False
  if person.prim.colliderect(vrag.prim):
     vrag.speed=[0,0]
     person.speed=[0,0]
     text = font.render('Ты проиграл', True, (255, 0, 0))
     win.blit(text, (220,150))
  text = font.render(str(ohki), True, (0, 0, 255))
  win.blit(text, (310,30))


  
  person.risshar()
  zemla.ris()
  vrag.ris()
  vrag.move()
  person.move()
  person.grav()

  pygame.display.update()
  clock.tick(scor+ohki)