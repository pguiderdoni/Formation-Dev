import pygame
import sys
import random



# Create the snake class - 2
class Snake:
    def __init__(self):
        self.length = 2
        self.position = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = (17, 24, 47)
        self.speed = 10
        self.score = 0

    def get_head_position(self):
        return self.position[0]

    def turn(self, point):
        if self.length > 1 and (-point[0], -point[1]) == self.direction:
            return
        else:
            self.direction=point
            print(point)

    def move(self):
        current_head_position = self.get_head_position()
        new_head_position = (current_head_position[0] + self.direction[0]*CASE_SIZE)%SCREEN_WIDTH, (current_head_position[1] + self.direction[1]*CASE_SIZE)%SCREEN_HEIGHT
        if self.length > 4 and new_head_position in self.position[4:]:
            self.reset() 
        else:
            self.position.insert(0, new_head_position)
            if len(self.position) > self.length:
                self.position.pop()
        
    def reset(self):
        self.length = 2
        self.position = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.score = 0
        self.speed = 10

    def draw(self, surface):
        for i in self.position:
            rectangle = pygame.Rect((i[0], i[1]), (CASE_SIZE, CASE_SIZE))
            pygame.draw.rect(surface, self.color, rectangle)

    def handle_key(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    self.turn(UP)
                elif event.key == pygame.K_s:
                    self.turn(DOWN)
                elif event.key == pygame.K_q:
                    self.turn(LEFT)
                elif event.key == pygame.K_d:
                    self.turn(RIGHT)
class Ennemy:
    def __init__(self):
        self.position = [((random.randint(0, CASE_WIDTH-1)*CASE_SIZE), (random.randint(0, CASE_HEIGHT-1)*CASE_SIZE))]
        self.color = "red"
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 3
        self.speed = 8

    def random_ennemy(self):
        self.position = ((random.randint(0, CASE_WIDTH-1)*CASE_SIZE), (random.randint(0, CASE_HEIGHT-1)*CASE_SIZE))

    def draw(self, surface):
        for i in self.position:
            rectangle = pygame.Rect((i[0], i[1]), (CASE_SIZE, CASE_SIZE))
            pygame.draw.rect(surface, self.color, rectangle)

    def reset(self):
        self.position = [((random.randint(0, CASE_WIDTH-1)*CASE_SIZE), (random.randint(0, CASE_HEIGHT-1)*CASE_SIZE))]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.length = 3
        self.speed = 8
        
    def get_head_position(self):
        return self.position[0]

    def move(self, nb_of_loops):
        if nb_of_loops % 8 == 0:
            self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        current_head_position = self.get_head_position()
        new_head_position = ((current_head_position[0] + self.direction[0]*CASE_SIZE)%SCREEN_WIDTH, (current_head_position[1] + self.direction[1]*CASE_SIZE)%SCREEN_HEIGHT)
        self.position.insert(0, new_head_position)
        if len(self.position) > self.length:
                self.position.pop()
        
        
        






# Create the food class - 2 bis
class Food:
    # Contructor - 10
    def __init__ (self):
        self.position = ((random.randint(0, CASE_WIDTH-1)*CASE_SIZE), (random.randint(0, CASE_HEIGHT-1)*CASE_SIZE))
        self.color = (233,163,49)
        # Fill the init method with food attributes : initial position and color - 39

    # Method to randomize a position for the food - 11
    def random_food(self):
       self.position = ((random.randint(0, CASE_WIDTH-1)*CASE_SIZE), (random.randint(0, CASE_HEIGHT-1)*CASE_SIZE))
        # Randomize the position - 40
    # Method to draw the food on the board - 12
    def draw(self, surface):
        rectangle = pygame.Rect((self.position[0], self.position[1]), (CASE_SIZE, CASE_SIZE))
        pygame.draw.rect(surface, self.color, rectangle)

        # Create and draw a rectangle of a different color for the food - 41


# Function to draw the grid - 17
def draw_grid(surface):
     # For each case of the grid - 18
    for y in range(0, int(CASE_HEIGHT)):
        for x in range(0, int(CASE_WIDTH)):
             # If we are on an even case of the grid, we create and draw a rectangle of a first color - 19
            if (x+y) %2 == 0:
                r = pygame.Rect((x*CASE_SIZE, y*CASE_SIZE), (CASE_SIZE, CASE_SIZE))
                pygame.draw.rect(surface, (80, 190, 200), r)
            else:
                rr = pygame.Rect((x*CASE_SIZE, y*CASE_SIZE), (CASE_SIZE, CASE_SIZE))
                pygame.draw.rect(surface, (80, 190, 200), rr)

   

           

            # Otherwise, we do the same with another color - 20


# Global variables (screen size, grid size, possible movements of the snake) - 13
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 640
CASE_SIZE = 20
CASE_WIDTH = SCREEN_WIDTH/CASE_SIZE
CASE_HEIGHT = SCREEN_HEIGHT/CASE_SIZE
UP=(0, -1)
DOWN=(0, 1)
RIGHT=(1, 0)
LEFT=(-1, 0)



def main():
    # Initialize the game - 14
    pygame.init()
    pygame.display.set_caption("Le gros Snake")
    # Set up (mettre en place) the clock and the screen - 15
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH), 0, 32)
    # Set up the game surface - 16
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    # Call the function that draws the grid - 21
    draw_grid(surface)
    # Create a snake and an initial food - 22
    snake=Snake()
    food=Food()
    ennemy=Ennemy()
    ennemy2=Ennemy()
    # Initiliaze the score - 23
    # Configure the font of the score - 47
    pygame.font.init()
    myfont = pygame.font.SysFont("monospace", 16)

    nb_of_loops = 0

    # The game loop - 24
    while (True):
        # pygame.time.wait(3000)
        # Choose the number of frames per second - 25
        clock.tick(snake.speed)
        # Handle the pressed keys - 42
        snake.handle_key()
        # Draw the grid - 43
        draw_grid(surface)
        # Move the snake - 44
        snake.move()
        ennemy.move(nb_of_loops)
        ennemy2.move(nb_of_loops)
        # Check if the snake's head is on a food - 45
        if snake.position[0] == food.position:
            snake.length+=1
            snake.score+=1
            food.random_food()
            snake.speed+=1
            ennemy.speed+=1
            if snake.speed>=30:
                snake.speed=30
            if ennemy.speed>=15:
                ennemy.speed=15
        for position in snake.position:
            if position in ennemy.position:
                snake.length +=1
                snake.score -=1
                ennemy.reset()  
            if position in ennemy2.position:
                snake.length +=1
                snake.score -=1
                ennemy2.reset()            
        # Draw the snake and the food - 46
        snake.draw(surface)
        food.draw(surface)
        ennemy.draw(surface)
        ennemy2.draw(surface)
        # Update and refresh the screen when an action occurs (a lieu) - 26
        screen.blit(surface, (0, 0))
        # Display the score on the top left corner - 48
        text=myfont.render("Score {0} ".format([snake.score]),1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()
        nb_of_loops += 1





if __name__ == "__main__":
    main()