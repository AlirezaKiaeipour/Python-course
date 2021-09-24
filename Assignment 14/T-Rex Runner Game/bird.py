import random
import arcade

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self,x,s):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture("img/bird0.png"),
                                    arcade.load_texture("img/bird1.png")]
        
        self.width = 50
        self.height = 50
        self.center_x = x
        self.center_y = random.randint(109,120)
        self.change_x -= s