import pygame
import math


def get_questions():
    questions = []

    for i in range(1, 30):
        question = input(f"Enter question {i} (or type 'exit' to stop): ")
        if question.lower() == 'exit':
            break
        questions.append(question)

    return questions

def main():
    print("Welcome to the Question Input App!")
    print("You can enter up to 2 questions. Type 'exit' to stop.")

    questions = get_questions()

    print("\nYou entered the following questions:")
    for i, question in enumerate(questions, start=1):
        print("{i}. {question}")
Q = get_questions()

pygame.init()

CLOCK = pygame.time.Clock()
FPS = 120



windowHeight = 400

windowWidth = 800

screen = pygame.display.set_mode((windowWidth, windowHeight)) # 0y(2nd parameter), top # 600y(2nd parameter), bottom # 0x(1st parameter), left # 800x(1st parameter), right
pygame.display.set_caption("MENTORIO")

MENTORIO_IMAGE = pygame.image.load("MENTORIO.png").convert()

MENTORIO_W = MENTORIO_IMAGE.get_width()

scroll = 0
tiles = math.ceil(windowWidth / MENTORIO_W)
print(tiles)

MENTORIO = pygame.image.load("MENTORIO.png")

pygame.display.set_icon(MENTORIO)

spriteTEST = pygame.Rect(10, 10, 50, 50)

start_time = pygame.time.get_ticks()

run = 1


while run == 1:

    CLOCK.tick(FPS)

    pygame.draw.rect(screen, (0, 0, 0), spriteTEST)

    screen.fill((0, 0, 0))

    

    if spriteTEST.x >= 800:
        run = 0
        print("YOU LOST")
        
    elif spriteTEST.y >= 400:

        run = 0
        print("YOU LOST")
        
    elif spriteTEST.y <= 0:

        run = 0
        print("YOU LOST")
        
    elif spriteTEST.x <= 0:

        run = 0
        print("YOU LOST")
       
    KEY_PRESSED = pygame.key.get_pressed()
    if KEY_PRESSED[pygame.K_w] == True:
        spriteTEST.move_ip(0, -2)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
        print(elapsed_time)
        print("SOLVING")
        print(Q)


    elif KEY_PRESSED[pygame.K_s] == True:
        spriteTEST.move_ip(0, +2)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
        print(elapsed_time)
        print("SOLVING")
        print(Q)
    

    elif KEY_PRESSED[pygame.K_a] == True:
        spriteTEST.move_ip(-2, 0)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
        print(elapsed_time)
        print("SOLVING")
        print(Q)

        

    elif KEY_PRESSED[pygame.K_d] == True:
        spriteTEST.move_ip(+2, 0)
        elapsed_time = (pygame.time.get_ticks() - start_time) / 1000.0
        print(elapsed_time)
        print("SOLVING")
        print(Q)

    for event in pygame.event.get():
    
       if event.type == pygame.QUIT:
           run = 0
pygame.display.update()  






    


        
    

 

   
  
         
        
        
    

     
            
      