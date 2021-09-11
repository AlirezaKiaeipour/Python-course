import arcade
class Circle(arcade.Sprite):
    def __init__(self):
        arcade.Sprite.__init__(self)
        self.col = 20
        self.row = 20
        self.center_x = 220
        self.center_y = 250

    def draw(self,x,y,i,j):
        if (i+j) % 2 == 0:
            arcade.draw_circle_filled(x,y,7,arcade.color.BLUE)
        else:
            arcade.draw_circle_filled(x,y,7,arcade.color.RED)

class Box(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,600,700,"Box Lopp")
        arcade.set_background_color(arcade.color.PINK)
        self.circle = Circle()

    def on_draw(self):
        arcade.start_render()
        for i in range(10):
            for j in range(10):
                center_x = j * self.circle.col + self.circle.center_x
                center_y = i * self.circle.row + self.circle.center_y
                self.circle.draw(center_x,center_y,i,j)
                
Box()
arcade.run()