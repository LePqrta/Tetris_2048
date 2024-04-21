<<<<<<< Updated upstream
=======

from game_grid import GameGrid # the class for modeling the game grid
from tetromino import Tetromino # the class for modeling the tetrominoes
import random # used for creating tetrominoes with random types/shapes
from scenes import *

# MAIN FUNCTION OF THE PROGRAM
#-------------------------------------------------------------------------------
# Main function where this program starts execution
def start():
   # Creating canvas
   grid_h, grid_w, grid = create_canvas(the_grid_height=20, the_grid_width=10, info_grid_width=4)
   
   # First tetromino gets created
   first_tetromino_shape = generate_next_tetromino_type()
   current_tetromino = create_tetromino(first_tetromino_shape)
   grid.current_tetromino = current_tetromino
   # Mext tetromino is created and shown
   next_tetromino_shape = generate_next_tetromino_type()
   next_tetromino_display = create_tetromino(next_tetromino_shape)
   grid.display_tetromino = next_tetromino_display


   # Menu getting displayed
   is_game_scene, game_speed = display_game_menu(grid_h, grid_w)
   do_reset = False
   # Clear the queue of the pressed keys for a smoother interaction
   stddraw.clearKeysTyped()
   # The main loop for interacting with the grid
   while True:
      if is_game_scene:
         # Checking user inputs
         if stddraw.hasNextKeyTyped():  # If a key is pressed
            key_typed = stddraw.nextKeyTyped() # That key is saved
            key_typed = "left"  if key_typed == "a" else key_typed
            key_typed = "right" if key_typed == "d" else key_typed
            key_typed = "down"  if key_typed == "s" else key_typed
            key_typed = "up"    if key_typed == "w" else key_typed
            # ESC ends the game
            if key_typed == "escape":
               is_game_scene = False
            # Left arrow key
            elif key_typed == "left":
               # Tetromino moves left by one
               current_tetromino.move(key_typed, grid) 
            # Right arrow key
            elif key_typed == "right":
               # Tetromino moves right by one
               current_tetromino.move(key_typed, grid)
            # Down arrow key
            elif key_typed == "down":
               # Tetromino moves down by one 
               # Tetromino falls faster than normal
               current_tetromino.move(key_typed, grid)
            elif key_typed == "space":
               # Tetromino drops as far as it can
               current_tetromino.hard_drop(grid)
               # Tetromino rotates clockwise
            elif key_typed == "e":
               current_tetromino.rotate_clockwise(grid)
               # Tetromino rotates counter-clockwise
            elif key_typed == "q" :
               current_tetromino.rotate_counter_clockwise(grid)
            elif key_typed == "p":
               do_reset = display_pause_menu(grid_h,grid_w)
            stddraw.clearKeysTyped()

         if do_reset:
            grid.reset_scene() # Tetrominos gets deleted from screen
            first_tetromino_shape = generate_next_tetromino_type()
            current_tetromino = create_tetromino(first_tetromino_shape)
            grid.current_tetromino = current_tetromino
            next_tetromino_shape = generate_next_tetromino_type()
            next_tetromino_display = create_tetromino(next_tetromino_shape)
            grid.display_tetromino = next_tetromino_display
            is_game_scene, game_speed = display_game_menu(grid_h, grid_w)
            stddraw.clearKeysTyped()
            do_reset = False
         else:
            # Tetromino moves down with each iteration
            success = current_tetromino.move("down",grid)

            # When the move is finished, next tetromino is placed on the grid
            if not success:
               tiles, pos = grid.current_tetromino.get_min_bounded_tile_matrix(True)
               game_over = grid.update_grid(tiles, pos)
               
               # Ending the game
               if game_over:
                  is_game_scene = False
               # Create the next tetromino to enter the game grid
               current_tetromino = create_tetromino(next_tetromino_shape)
               grid.current_tetromino = current_tetromino
               # The tetromino after that gets generated.
               next_tetromino_shape = generate_next_tetromino_type()
               next_tetromino_display = create_tetromino(next_tetromino_shape)
               grid.display_tetromino = next_tetromino_display
            # Game grid and the current tetromino gets displayed
            grid.display(game_speed)
      else: 
         grid.reset_scene() # Existing tetrominos gets removed
         first_tetromino_shape = generate_next_tetromino_type()
         current_tetromino = create_tetromino(first_tetromino_shape)
         grid.current_tetromino = current_tetromino
         next_tetromino_shape = generate_next_tetromino_type()
         next_tetromino_display = create_tetromino(next_tetromino_shape)
         grid.display_tetromino = next_tetromino_display
         is_game_scene = display_game_over(grid_h, grid_w)
         
         is_game_scene, game_speed = display_game_menu(grid_h, grid_w)
         stddraw.clearKeysTyped()

# Random next tetromino type is generated with this function
import random

def generate_next_tetromino_type():
   tetromino_types = ['I', 'O', 'Z', 'J', 'T', 'L', 'S']
   random_type = random.choice(tetromino_types)
   return random_type

# Function for creating a tetromino to enter the game grid from the given type
def create_tetromino(tetromino_type):
   # Tetromino and its type is created and returned
   tetromino = Tetromino(tetromino_type)
   return tetromino

# Function for creating the canvas for the game
def create_canvas(the_grid_height, the_grid_width, info_grid_width):
    # Grids dimensions are defined
    info_grid_w = info_grid_width
    grid_h, grid_w = the_grid_height, the_grid_width + info_grid_w
    # Canvas size
    canvas_h, canvas_w = 45 * grid_h, 45 * grid_w
    stddraw.setCanvasSize(canvas_w, canvas_h)
    # Scale of the coordinate system
    stddraw.setXscale(-1.5, grid_w + 0.5)
    stddraw.setYscale(-1.5, grid_h + 0.5)
    Tetromino.grid_height = grid_h
    Tetromino.grid_width = grid_w - info_grid_w
    grid = GameGrid(grid_h, grid_w - info_grid_w)
    return grid_h, grid_w, grid

if __name__== '__main__':
   start()
>>>>>>> Stashed changes
