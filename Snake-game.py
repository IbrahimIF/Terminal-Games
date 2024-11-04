class Snake:

    pass


class Apple:
    pass


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def render(self):
        print("height: ",  self.height)
        print("width: ",  self.width)
    pass

game =  Game(10, 20)
game.render()