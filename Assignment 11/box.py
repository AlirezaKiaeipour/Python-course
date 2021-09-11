import arcade

col = 25
row = 25
center_x = 200
center_y = 250

class Apple(arcade.Sprite):
    def __init__(self,x,y):
        arcade.Sprite.__init__(self)
        self.image = "image/apple.png"
        self.img = arcade.Sprite(self.image,0.03)
        self.img.center_x = x
        self.img.center_y = y

    def draw(self):
        self.img.draw()

class Pear(arcade.Sprite):
    def __init__(self,x,y):
        arcade.Sprite.__init__(self)
        self.image = "image/pear.png"
        self.img = arcade.Sprite(self.image,0.01)
        self.img.center_x = x
        self.img.center_y = y

    def draw(self):
        self.img.draw()
        

class Box(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,600,700,"Box Lopp")
        arcade.set_background_color(arcade.color.PINK)
        
    

    def on_draw(self):
        arcade.start_render()
        for i in range(10):
            for j in range(10):
                self.center_x = j * col + center_x
                self.center_y = i * row + center_y
                if (i+j) % 2 == 0:
                    self.apple = Apple(self.center_x,self.center_y)
                    self.apple.draw()
                else:
                    self.pear = Pear(self.center_x,self.center_y)
                    self.pear.draw()
                    
                
                
Box()
arcade.run()