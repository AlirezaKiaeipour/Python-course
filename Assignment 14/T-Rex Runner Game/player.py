import arcade


class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.walk_up_textures = [arcade.load_texture_pair("img/dino.png")] 
        self.walk_right_textures = [arcade.load_texture_pair("img/dino.png"),arcade.load_texture_pair("img/walk0.png"),arcade.load_texture_pair("img/walk1.png")]
        
    
        
        self.width = 100
        self.height = 100
        self.center_x = 150
        self.center_y = 300
        self.score = 0
        self.control_speed = 0 
        self.frame = 0

    def update_animation(self, delta_time: float = 1 / 60):
        if self.frame>=2:
            self.frame = 0
        else:
            self.frame +=1
            self.texture = self.walk_right_textures[self.frame][0]
        
        