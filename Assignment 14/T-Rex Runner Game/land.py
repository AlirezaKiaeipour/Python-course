import arcade


class Land(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(":resources:images/tiles/grassHalf_mid.png")
        self.width = 80
        self.height = 80
        self.center_x = x
        self.center_y = y
        