import arcade


class Onecoc(arcade.Sprite):
    def __init__(self,x):
        super().__init__("T-rex\smallcac.png")
        self.width = 20
        self.height = 40
        self.center_y = 65
        self.center_x = x
        self.speed = 3

    def move(self):
        self.center_x -= self.speed

    def control_speed(self,s):
        self.speed += s


class Twocac(arcade.Sprite):
    def __init__(self,x):
        super().__init__("T-rex\doublecac.png")
        self.width = 40
        self.height = 40
        self.center_x = x
        self.center_y = 65
        self.speed = 3

    def move(self):
        self.center_x -= self.speed

    def control_speed(self,s):
        self.speed += s

class Threecac(arcade.Sprite):
    def __init__(self,x):
        super().__init__("T-rex\cac.png")
        self.width = 65
        self.height = 40
        self.center_x = x
        self.center_y = 65
        self.speed = 3
    
    def move(self):
        self.center_x -= self.speed 

    def control_speed(self,s):
        self.speed += s

class Bird(arcade.AnimatedWalkingSprite):
    def __init__(self,x):
        super().__init__()

        self.stand_right_textures = [arcade.load_texture("T-rex\image1.png")]

        self.walk_right_textures = [arcade.load_texture("T-rex\image1.png"),
                                    arcade.load_texture("T-rex\image2.png")]

        self.stand_left_textures = [arcade.load_texture("T-rex\image1.png",mirrored=True)]

        self.walk_left_textures = [arcade.load_texture("T-rex\image1.png",mirrored=True),
                                    arcade.load_texture("T-rex\image2.png",mirrored=True)]


        self.width = 50
        self.height = 50
        self.center_x = x
        self.center_y = 100
        self.speed = 3

    def move(self):
        self.center_x -= self.speed

    def control_speed(self,s):
        self.speed += s