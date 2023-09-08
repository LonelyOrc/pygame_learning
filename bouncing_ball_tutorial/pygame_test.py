import sys, pygame # importing the necessary modules
pygame.init() # initializing the pygame modules for use in our program

size = width, height = 1920, 1080 # Setting the size of the display window
speed = [10, 10]

screen = pygame.display.set_mode(size) # Creating a graphical window - the display.set_mode() function
                                       # creates a new surface object that represents the actual displayed graphics.
                                       # Any drawing done will be visible on the monitor.

ball = pygame.image.load("intro_ball.gif") # Loading our image of a ball for use in the display
                                           # The pygame.image.load() function returns us a surface with the ball data.
                                           # The surface will keep any colorkey or alpha transparency from the file.

ballrect = ball.get_rect() # rect object type represents a rectangular area. 

# Pygame Game loop
while True:
    for event in pygame.event.get(): # checking for user input
        if event.type == pygame.QUIT: sys.exit() # if user click's the X on the application, the while loop exits
    
    ballrect = ballrect.move(speed) # Moving the ball by the current speed

    # reverse the speed if the ball has moved outside the screen. 
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    
    screen.fill("purple") # erase screen by filing it with purple color
    screen.blit(ball, ballrect) # surface.blit() method draws images. Blit means copying pixel colors from one image to another
                                # We pass the blit method a source surface to copy from, and a position to place the source onto 
                                # the destination
    pygame.display.flip() # This method allows what we've drawn on the screen surface to become visible. 
                          # Pygame manages the display with a double buffer. This buffering makes sure we only see completely drawn
                          # frames on the screen. Without it, the user would see the half completed parts of the screen as they are being
                          # created.