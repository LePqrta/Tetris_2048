import lib.stddraw as stddraw  # stddraw is used as a basic graphics library
from lib.color import Color # used for coloring the game grid
from point import Point  # used for tile positions
import numpy as np  # fundamental Python module for scientific computing
import copy 

# Class used for modelling the game grid
class GameGrid:
	# Constructor for creating the game grid based on the given arguments
   def __init__(self, grid_h, grid_w):
      # Setting the grid dimensions
      self.grid_height = grid_h
      self.grid_width = grid_w
      # Create a tile matrix to store the tiles landed onto the game grid
      self.tile_matrix = np.full((grid_h, grid_w), None)
      self.current_tetromino = None
      self.display_tetromino = None
      self.prediction_tetromino = None
      self.game_over = False
      self.score = 0
      # Empty grid cell color
      self.empty_cell_color = Color(205,193,180)
      # Colors used for grid lines and grid boundaries
      self.line_color = Color(187,172,161) 
      self.boundary_color = Color(119, 110, 101)
      # Thickness values for grid lines and boundaries
      self.line_thickness = 0.008
      self.box_thickness = 1 * self.line_thickness

   def eliminate_floating_pieces(self):
      self.check_connections()
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            if self.tile_matrix[row][col] is not None:
               if self.tile_matrix[row][col].is_connected == False:
                  self.drop_tile(row, col)
      self.check_connections()

   def check_connections(self):
      # Reset all the tiles
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            if self.tile_matrix[row][col] is not None:
               self.tile_matrix[row][col].is_connected = False
      # Tiles at the ground if they are connected
      for col in range(self.grid_width):
         if self.tile_matrix[0][col] is not None:
            self.tile_matrix[0][col].is_connected = True
      # Checking all the tiles above
      for row in range(1, self.grid_height):
         for col in range(self.grid_width):
            if self.tile_matrix[row][col] is not None:
               # Checking the neighbor below
               if self.tile_matrix[row - 1][col] is not None:
                  if self.tile_matrix[row - 1][col].is_connected == True:
                     self.tile_matrix[row][col].is_connected = True
                     continue
      for row in range(1, self.grid_height):
         for col in range(1, self.grid_width):
            if self.tile_matrix[row][col] is None:
               continue
            if self.tile_matrix[row][col - 1] is not None:
                  if self.tile_matrix[row][col - 1].is_connected == True:
                     self.tile_matrix[row][col].is_connected = True
                     continue
      for row in range(1, self.grid_height):
         for col in range(self.grid_width - 2, 0, -1):
            if self.tile_matrix[row][col] is None:
               continue 
            if self.tile_matrix[row][col + 1] is not None:
               if self.tile_matrix[row][col + 1].is_connected == True:
                  self.tile_matrix[row][col].is_connected = True
                  continue
   # Drop the tile to the ground
   def drop_tile(self, row, col):
      while self.tile_matrix[row-1][col] is None and row-1 >= 0:

         if col == 0:
            if self.tile_matrix[row][col+1] is not None:
               is_right_stable = self.tile_matrix[row][col+1].is_connected
               if is_right_stable:
                  return

         elif col == self.grid_width - 1:
            if self.tile_matrix[row][col-1] is not None:
               is_left_stable = self.tile_matrix[row][col-1].is_connected
               if is_left_stable:
                  return
         else:

            is_left_full = self.tile_matrix[row][col-1] is not None
            is_right_full = self.tile_matrix[row][col+1] is not None
            if is_left_full:
               is_left_stable = self.tile_matrix[row][col-1].is_connected
               if is_left_stable:
                  return
            if is_right_full:
               is_right_stable = self.tile_matrix[row][col+1].is_connected
               if is_right_stable:
                  return
         self.tile_matrix[row-1][col] = copy.deepcopy(self.tile_matrix[row][col])
         self.tile_matrix[row][col] = None
         row -= 1
         self.check_connections()

   def merge_tiles(self, row1, col1):
      if self.tile_matrix[row1][col1] is None:
         return False

      if self.tile_matrix[row1][col1] is not None and self.tile_matrix[row1+1][col1] is not None:
         # Numbers are matching > merge
         if row1+1 < self.grid_height and self.tile_matrix[row1][col1].number == self.tile_matrix[row1+1][col1].number:
               self.tile_matrix[row1][col1].number *= 2
               self.score += self.tile_matrix[row1][col1].number
               self.tile_matrix[row1+1][col1] = None
               self.check_connections()
               while row1-1 >= 0 and self.tile_matrix[row1-1][col1] is None:
                  self.check_connections()
                  if col1 == 0:
                     if self.tile_matrix[row1][col1+1] is not None:
                           break
                  if col1 == self.grid_width - 1:
                     if self.tile_matrix[row1][col1-1] is not None:
                           break
                  is_left_full = self.tile_matrix[row1][col1-1] is not None
                  is_right_full = self.tile_matrix[row1][col1+1] is not None
                  if is_left_full or is_right_full:
                     break
                  self.tile_matrix[row1-1][col1] = self.tile_matrix[row1][col1]
                  self.tile_matrix[row1][col1] = None
                  row1 -= 1
                  self.check_connections()
               return True
         return False

   def merge_possible(self):
      for row in range(self.grid_height - 1):
         for col in range(self.grid_width):
               below_check = self.tile_matrix[row][col] is not None
               after_check = self.tile_matrix[row+1][col] is not None

               if below_check and after_check:
                  if self.tile_matrix[row][col].number == self.tile_matrix[row+1][col].number:
                     return True, row, col

      return False, -1, -1


   # Method used for resetting the game environment
   def reset_scene(self):
      self.tile_matrix = np.full((self.grid_height, self.grid_width), None)
      self.current_tetromino = None
      self.display_tetromino = None
      self.score = 0
      self.game_over = False

   # Method used for displaying the game grid
   def display(self, speed=100):
      # Background clear
      stddraw.clear(Color(169, 150, 151))

      self.draw_grid()
      if self.current_tetromino is not None:
         self.current_tetromino.draw()
      if self.display_tetromino is not None:
         self.display_tetromino.bottom_left_cell = Point()
         self.display_tetromino.bottom_left_cell.y = self.grid_height - 4
         self.display_tetromino.bottom_left_cell.x = self.grid_width + 1
         stddraw.text(self.grid_width + 2, self.grid_height - 5.15, "Next Piece")
         self.display_tetromino.draw(next_display=True)
      self.draw_boundaries()
      stddraw.show(speed)
   def display_score(self):
      stddraw.setFontSize(28)
      stddraw.setPenColor(Color(69, 60, 51))
      stddraw.text(self.grid_width + 2, self.grid_height // 2, "Score")
      stddraw.setFontFamily("Arial")
      stddraw.text(self.grid_width + 2, self.grid_height // 2 - 0.8, str(self.score))
      stddraw.setFontFamily("Aharoni")


   # Method for drawing the cells and the lines of the game grid
   def draw_grid(self):
      start_x, end_x = -0.5, self.grid_width - 0.5
      start_y, end_y = -0.5, self.grid_height - 0.5
      stddraw.setPenColor(self.empty_cell_color)
      stddraw.filledRectangle(start_x,start_y,end_x+0.5,end_y+0.5)
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            if self.tile_matrix[row][col] is not None:
               self.tile_matrix[row][col].draw(Point(col, row))
      self.display_score()

      stddraw.setPenColor(self.line_color)
      stddraw.setPenRadius(self.line_thickness)

      start_x, end_x = -0.5, self.grid_width - 0.5
      start_y, end_y = -0.5, self.grid_height - 0.5
      for x in np.arange(start_x + 1, end_x, 1):  
         stddraw.line(x, start_y, x, end_y)
      for y in np.arange(start_y + 1, end_y, 1):  
         stddraw.line(start_x, y, end_x, y)
      stddraw.setPenRadius()           
      
   # Method for drawing the boundaries around the game grid 
   def draw_boundaries(self):
      stddraw.setPenColor(self.boundary_color)  
      stddraw.setPenRadius(self.box_thickness)
      pos_x, pos_y = -0.6, -0.6
      stddraw.rectangle(pos_x, pos_y, self.grid_width + 0.15, self.grid_height + 0.15)
      stddraw.setPenRadius()  

   # Method used for checking whether the grid cell with given row and column 
   # Indexes is occupied by a tile or empty
   def is_occupied(self, row, col):
      if not self.is_inside(row, col):
         return False
      return self.tile_matrix[row][col] is not None
      
   def is_inside(self, row, col):
      if row < 0 or row >= self.grid_height:
         return False
      if col < 0 or col >= self.grid_width:
         return False
      return True

   def is_row_full(self, row):
      for col in range(self.grid_width):
         if self.tile_matrix[row][col] is None:
            return False
      return True

   #  Row gets removed if it is full
   def remove_row(self, row):
      for col in range(self.grid_width):
         self.score += self.tile_matrix[row][col].number
         self.tile_matrix[row][col] = None

   def shift_rows_down(self, row):
      for i in range(row + 1, self.grid_height):
         for col in range(self.grid_width):
            self.tile_matrix[i - 1][col] = self.tile_matrix[i][col]
            self.tile_matrix[i][col] = None

   def remove_full_rows(self):
      for row in range(self.grid_height):
         while self.is_row_full(row):
            self.remove_row(row)
            self.shift_rows_down(row)

   # Method that locks the tiles of the landed tetromino on the game grid while
   # Checking if the game is over due to having tiles above the topmost grid row.
   # The method returns True when the game is over and False otherwise.
   def update_grid(self, tiles_to_lock, blc_position):
      self.current_tetromino = None 
      n_rows, n_cols = len(tiles_to_lock), len(tiles_to_lock[0])
      for col in range(n_cols):
         for row in range(n_rows):            
            if tiles_to_lock[row][col] is not None:
               # Pos of the tile
               pos = Point()
               pos.x = blc_position.x + col
               pos.y = blc_position.y + (n_rows - 1) - row
               if self.is_inside(pos.y, pos.x):
                  self.tile_matrix[pos.y][pos.x] = tiles_to_lock[row][col]
               # Game ends 
               else:
                  self.game_over = True
                  self.score = 0

      # Merging
      self.eliminate_floating_pieces()
      is_merge_possible, row1, col1 = self.merge_possible()
      while is_merge_possible:
         self.merge_tiles(row1, col1)
         self.eliminate_floating_pieces()
         is_merge_possible, row1, col1 = self.merge_possible()
      # After merging is done
      self.remove_full_rows()
      return self.game_over

