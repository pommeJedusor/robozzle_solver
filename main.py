import pygame

WIDTH = 16
HEIGHT = 12

def ungrey(grid):
    for i in range(81):
        if grid[i]==-1:
            grid[i]=1

def up_color_square(pos, grid, robozzle_squares):
    for i in range(WIDTH*HEIGHT):
        if robozzle_squares[i].collidepoint(pos):
            if grid[i]==-1:
                ungrey(grid)
                return   
            grid[i] +=1
            return

def down_color_square(pos, grid, robozzle_squares):
    for i in range(WIDTH*HEIGHT):
        if robozzle_squares[i].collidepoint(pos):
            grid[i] -=1
            return


def update_view(screen, blockudoku_board, blockudoku_squares):
    screen.fill("yellow")
    #update the view of the grid
    pygame.draw.rect(screen, "black", blockudoku_board)
    for i in range(WIDTH*HEIGHT):
        if grid[i]==-1:
            pygame.draw.rect(screen, "grey", blockudoku_squares[i])
        elif grid[i]==0:
            pygame.draw.rect(screen, "black", blockudoku_squares[i])
        elif grid[i]==1:
            pygame.draw.rect(screen, "blue", blockudoku_squares[i])
        elif grid[i]==2:
            pygame.draw.rect(screen, "green", blockudoku_squares[i])
        elif grid[i]==3:
            pygame.draw.rect(screen, "red", blockudoku_squares[i])
        pygame.draw.rect(screen, "black", blockudoku_squares[i], 1)
    

pygame.init()
screen = pygame.display.set_mode((1920, 990))
clock = pygame.time.Clock()
running = True

robozzle_board = pygame.Rect(0, 0, (990/HEIGHT)*WIDTH, 990)
robozzle_squares = []
grid = [0 for i in range(WIDTH*HEIGHT)]

size = 990/HEIGHT
for y in range(HEIGHT):
    for x in range(WIDTH):
        robozzle_squares.append(pygame.Rect(size*x, size*y, size, size))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            numButton = event.button
            print(numButton)
            if numButton == 1:
                up_color_square(pos, grid, robozzle_squares)
            elif numButton == 3:
                down_color_square(pos, grid, robozzle_squares)
                    

    # update the view
    update_view(screen, robozzle_board, robozzle_squares)



    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60
    dt = clock.tick(60) / 1000

pygame.quit()
