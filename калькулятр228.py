import pygame
def MOUSEOVERnumbers():
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()          
        if s_1s.isOver(pos):
            print("1")
        if s_2s.isOver(pos):
            print("2")
        if s_3s.isOver(pos):
            print("3")
        if s_4s.isOver(pos):
            print("4")
        if s_5s.isOver(pos):
            print("5")
        if s_6s.isOver(pos):
            print("6")
        if s_7s.isOver(pos):
            print("7")
        if s_8s.isOver(pos):
            print("8")
        if s_9s.isOver(pos):
            print("9")
        if s_0s.isOver(pos):
            print("0")            
class rect():
    def __init__(self, color, x,y,width,height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.over = False
root = pygame.display.set_mode((400,620))
pygame.display.set_caption('калькулятор мега ультра про+ version 24343534.768')
image = pygame.image.load('калькулятор.jpg')
s_1s = rect((0,255,0),40,450,30,30, '1')
s_2s = rect((0,255,0),40,400,30,30, '2')
s_3s = rect((0,255,0),40,350,30,30, '3')
s_4s = rect((0,255,0),100,450,30,30, '4')
s_5s = rect((0,255,0),100,400,30,30, '5')
s_6s = rect((0,255,0),100,350,30,30, '6')
s_7s = rect((0,255,0),150,450,30,30, '7')
s_8s = rect((0,255,0),150,400,30,30, '8')
s_9s = rect((0,255,0),150,350,30,30, '9')
s_0s = rect((0,255,0),200,450,30,30, '0')
root.blit(image,(0,0))
for event in pygame.event.get():
        if event.type == pygame.QUIT:
                exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Нажата кнопка: ", event.button)
pygame.display.update()
run = True
while run:
        

        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                run = False


pygame.quit()
