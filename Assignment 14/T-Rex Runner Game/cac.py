import arcade

class Onecoc(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("img/cac0.png")
        self.width = 20
        self.height = 40
        self.center_y = 65
        self.center_x = x
        self.change_x -= s

class Twocac(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("img/cac1.png")
        self.width = 40
        self.height = 40
        self.center_x = x
        self.center_y = 65
        self.change_x -= s

class Threecac(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("img/cac2.png")
        self.width = 65
        self.height = 40
        self.center_x = x
        self.center_y = 65
        self.change_x -= s