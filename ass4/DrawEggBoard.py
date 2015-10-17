#! /usr/bin/env/python3


from PIL import Image
from PIL import ImageDraw
from EggBoard import Board

class DrawBoard:
    """Module to make a visualisation of the board"""
    
    def __init__(self, board):
        self.board = board.get_board()
        self.tile_size = 20 # size of each row/column in pixels
        self.board_width = len(self.board[0])
        self.board_height = len(self.board)
        image_size = (self.board_width * self.tile_size,
                      self.board_height * self.tile_size)
        self.board_image = Image.new("RGB", image_size, "white")
    
    def show(self):
        self.board_image.show()
    
    def save(self, filename):
        self.board_image.save(filename)
        
    def draw_board(self):
        draw = ImageDraw.Draw(self.board_image)
        
        for y in range(self.board_height):
            for x in range(self.board_width):
                coord = (x * self.tile_size, y * self.tile_size,
                         (x+1) * self.tile_size, (y+1) * self.tile_size)
                
                draw.rectangle(coord, fill="white", outline="black")
     
    def draw_eggs(self):
        draw = ImageDraw.Draw(self.board_image)
        
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                if self.board[y][x]:
                    ts = self.tile_size
                    coord = (x * ts + int(ts*0.2), y * ts + int(ts*0.1),
                             (x+1) * ts - int(ts*0.2), (y+1) * ts - int(ts*0.1))
                    
                    draw.ellipse(coord, fill="brown", outline="black")


if __name__ == "__main__":
    from Problem1 import Problem1 as P
    b = P(5, 5, 2)
    b.populate_board()
    b.print_board(b.board)
    db = DrawBoard(b.board)
    db.draw_board()
    db.draw_eggs()
    db.show()
