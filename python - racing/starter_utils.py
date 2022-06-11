# Import essential modules - 34
from pygame.transform import scale, rotate
# Function to scale the image by a given factor - 35
def scale_image(image, factor):
    # Calculate the new size of the image given the scale factor - 36
    new_size = round(image.get_width() * factor), round(image.get_height() * factor)
    # Scale the image - 37
    return scale(image, new_size)
# Function to rotate the image of the car - 41
def blit_rotate_center(screen, image, top_left, angle):
    # Rotate the image by the angle - 42
    rotated_image = rotate(image, angle)
    # Update the "hitbox" of the car - 43
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=top_left).center)
    # Display them on the screen - 44
    screen.blit(rotated_image, new_rect.topleft)

# Create a function to display a text at the center of the screen - 84
def blit_text_center(screen, font, text):
    render = font.render(text, 1, (255, 255,255))
    screen.blit(render, (screen.get_width()/2 - render.get_width()/2, screen.get_height()/2.5 - render.get_height()/2.5 ))


