import lib.stddraw as stddraw  # stddraw is used as a basic graphics library
from lib.color import Color  # used for coloring the tile and the number on it
import random

# Class used for modeling numbered tiles as in 2048
class Tile: 
   # Class attributes shared among all Tile objects
   # ---------------------------------------------------------------------------
   # the value of the boundary thickness (for the boxes around the tiles)
   boundary_thickness = 0.004
   # font family and size used for displaying the tile number
   font_family = "italic"

   # Constructor that creates a tile with 2 as the number on it
   def __init__(self):
      # set the number on the tile
      self.number = 2 if random.randint(0,10) < 8 else 4
      # set the colors of the tile
      self.background_color = Color(50, 30, 32) # background (tile) color
      self.foreground_color = Color(1, 21, 31) # foreground (number) color
      self.box_color = Color(160, 71, 225) # box (boundary) color
      self.font_size = 25
      self.is_connected = False
      self.colors = {
         2: {
            'color': Color(196, 228, 218),
            'font': 25
            },
         4: {
            'color': Color(209, 227, 217),
            'font': 25
            },
         8: {
            'color': Color(243, 178, 122),
            'font': 25
            },
         16: {
            'color': Color(246, 150, 100),
            'font': 25
            },
         32: {
            'color': Color(78, 228, 218),
            'font': 25
            },
         64: {
            'color': Color(247, 95, 59),
            'font': 25
            },
         128: {
            'color': Color(237, 28, 115),
            'font': 20
            },
         256: {
            'color': Color(237, 204, 98),
            'font': 20
            },
         512: {
            'color': Color(210, 201, 80),
            'font': 20
            },
         1024: {
            'color': Color(287, 157, 63),
            'font': 16
            },
         2048: {
            'color': Color(3, 28, 146),
            'font': 16
            }
      }

   def draw(self, position, length=1.05, is_pred=False, next=False):
    # draw the tile as a filled square
    if is_pred:
        stddraw.setPenColor(Color(42, 69, 99))
    else:
        pink_color = Color(255, 192, 203)  # Pink color
        stddraw.setPenColor(pink_color)
    stddraw.filledSquare(position.x, position.y, length / 2)
    # draw the bounding box around the tile as a square
    if is_pred:
        stddraw.setPenColor(Color(151, 178, 199))
    else:
        stddraw.setPenColor(self.box_color)
    stddraw.setPenRadius(Tile.boundary_thickness)
    stddraw.square(position.x, position.y, length / 2)
    stddraw.setPenRadius()  # reset the pen radius to its default value
    if not next:
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(self.font_size)
        stddraw.text(position.x, position.y, str(self.number))
    stddraw.setPenRadius() 