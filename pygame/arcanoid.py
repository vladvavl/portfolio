#портфолио
import pygame
import random    

# Устанавливаем размеры окна
shir = 900  
wish = 600 
win = pygame.display.set_mode((shir, wish))
pygame.display.set_caption("арканоид")  # Устанавливаем заголовок окна
pygame.init()  # Инициализируем Pygame

# Определение цветов
white = (255, 255, 255)
green = (86, 201, 197)
black = (0, 0, 0)
red = (255, 0, 0)

clock = pygame.time.Clock()  # Создаем объект Clock для управления временем в игре

# Загрузка фона
fon = pygame.image.load("fon2.jpg").convert()
fon = pygame.transform.scale(fon, (shir, wish))
class Obekt:
    def __init__(self, shir, wish, x, y, cvet) -> None:
        self.shir = shir  # Ширина объекта
        self.wish = wish  # Высота объекта
        self.x = x  # Координата X объекта на экране
        self.y = y  # Координата Y объекта на экране
        self.cvet = cvet  # Цвет объекта
        self.prim = pygame.Rect(self.x, self.y, self.shir, self.wish)  # Прямоугольник, описывающий объект на экране
    
    def ris(self):  # Метод для отрисовки прямоугольника
        pygame.draw.rect(win, self.cvet, self.prim)

    def risshar(self):  # Метод для отрисовки эллипса
        pygame.draw.ellipse(win, self.cvet, self.prim)


def colishen(scorx,scory,shar,predm):
    if scorx>0:
        dx=shar.prim.right-predm.prim.left
    else :
        dx=predm.prim.right-shar.prim.left
    if scory>0:
        dy=shar.prim.bottom-predm.prim.top
    else :
        dy=predm.prim.bottom-shar.prim.top
    if dx>dy:
        scory=-scory
    elif dy>dx:
        scorx=-scorx
    return scorx ,scory
    
    


# Создаем объекты класса Obekt
plotf = Obekt(300, 30, 290, 400, green)  # Платформа
shar = Obekt(50, 50, 420, 300, red)  # Шар
#враги
vragi = []
# Создаем три ряда врагов
for i in range(3):
    for j in range(10):  # Создаем 10 врагов в каждом ряду
        vrag= Obekt(50, 30, 50 + j * 80, 50 + i * 50, red)  # Создаем объект врага
        vragi.append(vrag)  # Добавляем врага в список
skorx=5
skory=5
ohci = 0
kadr=30
font = pygame.font.Font(None, 80)

# Главный игровой цикл
while True:
    win.blit(fon, (0, 0))  # Отображаем фон
    for event in pygame.event.get():  # Проверяем события
        if event.type == pygame.QUIT:  # Если пользователь закрыл окно
            pygame.quit()  # Завершаем Pygame
            exit()  # Завершаем программу
        
    
    shar.prim.x+=skorx
    shar.prim.y+=skory

    if shar.prim.colliderect(plotf.prim):
        skorx,skory=colishen(skorx,skory,shar,plotf)
    if shar.prim.x<0 or shar.prim.right>shir:
        skorx*=-1
    if shar.prim.y<0 :
        skory*=-1
    if shar.prim.y>wish:
        skorx,skory=0,0
        
        
        text = font.render('Ты проиграл', True, (255, 0, 0))
        win.blit(text, (shir/2,wish/2))
       


    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        plotf.prim.x-=5
    elif keys[pygame.K_RIGHT]:
        plotf.prim.x+=5
    if plotf.prim.right<0:
        plotf.prim.left=shir
    if plotf.prim.left>shir:
        plotf.prim.right=0

    
    for vrag in vragi:
        vrag.ris()
        if vrag.prim.colliderect(shar.prim):
            skorx,skory=colishen(skorx,skory,shar,vrag)
            vragi.remove(vrag)
            ohci+=1
    
    
    plotf.ris()  # Отрисовываем платформу
    shar.risshar()  # Отрисовываем шар
    text = font.render(str(ohci), True, (0, 0, 255))
    win.blit(text, (shir/2,500))
    if len(vragi)==0:
        skorx,skory=0,0
        shar.prim.y,shar.prim.x=wish/2,shir/2
        text = font.render('Победа', True, (0, 0, 255))
        win.blit(text, (shir/2,wish/2))
    
    pygame.display.update()  # Обновляем экран
    clock.tick(kadr+ohci)  # Устанавливаем частоту кадров в секунду