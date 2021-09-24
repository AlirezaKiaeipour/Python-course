import arcade

class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.stand_right_textures = [arcade.load_texture("img/dino.png")]

        self.walk_right_textures = [arcade.load_texture("img/walk0.png"),
                                    arcade.load_texture("img/walk1.png")]
        self.walk_up_textures = [arcade.load_texture("img/dino.png")]
        
        self.width = 100
        self.height = 100
        self.center_x = 150
        self.center_y = 300
        self.score = 0
        self.control_speed = 0 
        