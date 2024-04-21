import lib.stddraw as stddraw
from lib.picture import Picture  # Used for showing images
from lib.color import Color  # Used for game menu
import os  # Used for directory operations

# Displaying main menu
def display_game_menu(grid_height, grid_width):
   # Background color
   background_color = Color(238, 228, 218)
   # Button color
   button_color = Color(255, 0, 255)
   # Text color
   text_color = Color(255, 255, 255)
   # Change the background color
   stddraw.clear(background_color)
   # Getting the directory of the current directory to reach image file 
   current_dir = os.path.dirname(os.path.realpath(__file__))
   # Saving the path of the image
   img_file = current_dir + "/images/menu_image.png"
   # Center coordinates
   img_center_x, img_center_y = (grid_width - 1) / 2, grid_height - 7
   image_to_display = Picture(img_file)
   # Image getting displayed
   stddraw.picture(image_to_display, img_center_x, img_center_y)
   # Start game button 
   button_w, button_h = grid_width - 8, 2
   # Coordinates of the bottom left corner of the start game button 
   button_main_blc_x, button_main_blc_y = img_center_x - button_w / 2, 4
   button_start_blc_x, button_start_blc_y = img_center_x - button_w / 4, 4
   # Display the start button
   stddraw.setPenColor(button_color)
   stddraw.filledRectangle(button_main_blc_x, button_main_blc_y, button_w, button_h)
   # Text on the start button
   stddraw.setFontFamily("italic")
   stddraw.setFontSize(40)
   stddraw.setPenColor(text_color)
   text_to_display = "Start the Game"
   stddraw.text(img_center_x, 5, text_to_display)
   game_speed = 250
   # Menu's interaction loop
   while True:
      stddraw.show(50)
      if stddraw.mousePressed():
         mouse_x, mouse_y = stddraw.mouseX(), stddraw.mouseY()
         if mouse_x >= button_main_blc_x and mouse_x <= button_main_blc_x + button_w:
            if mouse_y >= button_main_blc_y and mouse_y <= button_main_blc_y + button_h:
               stddraw.clear(background_color)
               current_dir = os.path.dirname(os.path.realpath(__file__))
               img_file = current_dir + "/images/controls-v6.png"
               image_to_display = Picture(img_file)
               stddraw.picture(image_to_display, img_center_x, img_center_y + 2)
               stddraw.setPenColor(button_color)
               stddraw.filledRectangle(button_start_blc_x,     button_start_blc_y,     button_w / 2, button_h)
               stddraw.setFontSize(36)
               stddraw.setPenColor(text_color)
               stddraw.text(img_center_x,5, "Start")
               stddraw.show(50)
               while True:
                  stddraw.show(50)
                  # If mouse is left clicked
                  if stddraw.mousePressed():
                     # Getting the coordinates of the last left click
                     mouse_x, mouse_y = stddraw.mouseX(), stddraw.mouseY()
                     # Check if these coordinates are inside the button
                     if mouse_x >= button_start_blc_x and mouse_x <= button_start_blc_x + button_w / 2:
                        if mouse_y >= button_start_blc_y and mouse_y <= button_start_blc_y + button_h:
                           # Start the game 
                           game_speed = 250
                           break
               break
   return True, game_speed

# Function for displaying a simple menu after the game is over
def display_game_over(grid_height, grid_width):
   # Background color
   background_color = Color(238, 228, 218)
   # Button color
   button_color = Color(255, 0, 255)
   # Text color
   text_color = Color(238, 228, 218)
   # Change the background color
   stddraw.clear(background_color)
   # Center coordinates of the image
   img_center_x, img_center_y = (grid_width - 1) / 2, grid_height - 7
   button_w, button_h = grid_width - 8, 2
   button_blc_x, button_blc_y = img_center_x - button_w / 2, 6
   stddraw.setPenColor(button_color)
   stddraw.filledRectangle(button_blc_x, button_blc_y, button_w, button_h)
   stddraw.setFontFamily("Aharoni")
   stddraw.setFontSize(40)
   stddraw.setPenColor(text_color)
   text_to_display = "Restart"
   stddraw.text(img_center_x, 7, text_to_display)
   text_to_show = "Game Over"
   stddraw.setPenColor(button_color)
   stddraw.setFontSize(72)
   stddraw.text(img_center_x, grid_height*3//4 - 1, text_to_show)
   stddraw.setFontSize(24)
   # Menu's interaction loop
   while True:
      stddraw.show(50)
      # If mouse is left clicked
      if stddraw.mousePressed():
         # Getting the coordinates of the last left click
         mouse_x, mouse_y = stddraw.mouseX(), stddraw.mouseY()
         # Check if these coordinates are inside the button
         if mouse_x >= button_blc_x and mouse_x <= button_blc_x + button_w:
            if mouse_y >= button_blc_y and mouse_y <= button_blc_y + button_h: 
               do_restart = True
               break
   return True

def display_pause_menu(grid_height, grid_width):
   # Background color
   background_color = Color(238, 228, 218)
   # Button color
   button_color = Color(255, 0, 255)
   # Text color
   text_color = Color(238, 228, 218)
   # Change the background color 
   stddraw.clear(background_color)
   # Getting the directory of the current directory to reach image file 
   current_dir = os.path.dirname(os.path.realpath(__file__))
   # Saving the path of the image
   img_file = current_dir + "/images/menu_image.png"
   # Image coordinates
   img_center_x, img_center_y = (grid_width - 1) / 2, grid_height - 7
   image_to_display = Picture(img_file)
   # Display the image
   stddraw.picture(image_to_display, img_center_x, img_center_y)
   button_w, button_h = grid_width - 8, 2
   button_blc_x, button_blc_y = img_center_x - button_w / 2, 4
   button_res_blc_x, button_res_blc_y = img_center_x - button_w / 2, 1
   stddraw.setPenColor(button_color)
   stddraw.filledRectangle(button_blc_x, button_blc_y, button_w, button_h)
   stddraw.filledRectangle(button_res_blc_x, button_res_blc_y, button_w, button_h)
   stddraw.setFontFamily("Aharoni")
   stddraw.setFontSize(40)
   stddraw.setPenColor(text_color)
   text_to_display = "Resume"
   stddraw.text(img_center_x, 5, text_to_display)
   stddraw.text(img_center_x, 2, "Restart")

   do_reset = False

   # Menu loop
   while True:
      stddraw.show(50)
      # If mouse is left clicked
      if stddraw.mousePressed():
          # Getting the coordinates of the last left click
         mouse_x, mouse_y = stddraw.mouseX(), stddraw.mouseY()
         # Check if these coordinates are inside the button
         if mouse_x >= button_blc_x and mouse_x <= button_blc_x + button_w:
            if mouse_y >= button_blc_y and mouse_y <= button_blc_y + button_h:
               do_reset = False
               break 
         if mouse_x >= button_res_blc_x and mouse_x <= button_res_blc_x + button_w:
            if mouse_y >= button_res_blc_y and mouse_y <= button_res_blc_y + button_h:
               do_reset = True
               break 
   return do_reset