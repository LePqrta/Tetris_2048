
import lib.stddraw as stddraw  # stddraw library is used as a basic graphics 
from lib.color import Color  # used for coloring the tile and the number on it as understandable from the name
import random

# Class used for modeling numbered tiles as in 2048
class Tile: 
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # Tiles' boundaries's thickness
   boundary_thickness = 0.004
   font_family = "italic"  # Font is italic

   # Constructor that creates a tile with 2 as the number on it(min number is 2)
   def __init__(self):
      # Number is set here
      self.number = 2 if random.randint(0,10) < 8 else 4
      self.background_color = Color(50, 30, 32) # background (tile) color
      self.foreground_color = Color(1, 21, 31) # foreground (number) color
      self.box_color = Color(160, 71, 225) # box (boundary) color
      self.font_size = 25
      self.is_connected = False
      

   # Draw method
   def draw(self, position, length=1.05, is_pred=False, next=False):
    # draw the tile as a filled square
    if is_pred:
        stddraw.setPenColor(Color(42, 69, 99))
    else:
        pink_color = Color(255, 192, 203)  # Pink color code // sets the colors to pink
        stddraw.setPenColor(pink_color)
    stddraw.filledSquare(position.x, position.y, length / 2)
     # drawing part
    # draw the bounding box around the tile as a square
    if is_pred:
        stddraw.setPenColor(Color(151, 178, 199))
    else:
        stddraw.setPenColor(self.box_color)
    stddraw.setPenRadius(Tile.boundary_thickness)
    stddraw.square(position.x, position.y, length / 2)
    stddraw.setPenRadius()  # reseting the pen radius to the default value
    if not next:
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(self.font_size)
        stddraw.text(position.x, position.y, str(self.number))
    stddraw.setPenRadius() 

