import random
import time
import arcade


class Snake(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.GREEN
        self.speed = 3
        self.width = 16
        self.height = 16
        self.r = 8
        self.center_x = w // 2
        self.center_y = h // 2
        self.change_x = 0 
        self.change_y = 0
        self.score = 1
        self.body = []
        self.length = 0
        
    def draw(self):
        arcade.draw_circle_filled(self.center_x,self.center_y,self.r,self.color)
        self.body.append([self.center_x,self.center_y])
        for i in self.body:
            arcade.draw_circle_filled(i[0],i[1],self.r,self.color)
        if len(self.body) > self.length:
            self.body.pop(0)

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def eat_pear(self):
        self.score += 2 
    
    def eat_bomb(self):
        self.score -= 1

    def eat_apple(self):
        self.score += 1
        self.length +=1

class Apple(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.image = "image/apple.png"
        self.img = arcade.Sprite(self.image,0.03)
        self.img.center_x = random.randint(1,w)
        self.img.center_y = random.randint(1,h) 

    def draw(self):
        self.img.draw()

class Pear(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.image = "image/pear.png"
        self.img = arcade.Sprite(self.image,0.01)
        self.img.center_x = random.randint(1,w)
        self.img.center_y = random.randint(1,h)

    def draw(self):
        self.img.draw()

class Bomb(arcade.Sprite):
    def __init__(self,w,h):
        arcade.Sprite.__init__(self)
        self.image = "image/bomb.png"
        self.img = arcade.Sprite(self.image,0.04)
        self.img.center_x = random.randint(1,w)
        self.img.center_y = random.randint(1,h)

    def draw(self):
        self.img.draw()

class Game(arcade.Window):
    def __init__(self):
        arcade.Window.__init__(self,750,650,"Snake Game")
        self.background = arcade.load_texture("image/sand.jpg")
        self.apple = Apple(750,650)
        self.pear = Pear(750,650)
        self.bomb = Bomb(750,650)
        self.snake = Snake(750,650)
        self.score_txt = None
        self.score_txt = arcade.Camera(self.width,self.height)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_texture_rectangle(0,200,1920,1080,self.background)
        self.apple.draw()
        self.pear.draw()
        self.bomb.draw()
        self.snake.draw()
        self.score_txt.use()
        score_text = f"Score: {self.snake.score}"
        arcade.draw_text(score_text,10,630,arcade.color.RED,15)
        if 0 >= self.snake.center_x or self.snake.center_x >= 750:
            self.lost = f"GAME OVER"
            time.sleep(1)
            arcade.exit()
            arcade.draw_text(self.lost,250,320,arcade.color.RED,30)
        elif 0 >= self.snake.center_y or self.snake.center_y >= 650:
            self.lost = f"GAME OVER"
            arcade.draw_text(self.lost,250,320,arcade.color.RED,30)
            time.sleep(1)
            arcade.exit()
        elif self.snake.score <=0:
            self.lost = f"GAME OVER"
            arcade.draw_text(self.lost,250,320,arcade.color.RED,30)
            time.sleep(1)
            arcade.exit()
               
    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake,self.pear.img):
            self.snake.eat_pear()
            self.pear = Pear(750,650)
        elif arcade.check_for_collision(self.snake,self.bomb.img):
            self.snake.eat_bomb()
            self.bomb = Bomb(750,650)
        elif arcade.check_for_collision(self.snake,self.apple.img):
            self.snake.eat_apple()
            self.apple = Apple(750,650)

    def on_key_release(self,key,modifiers):
        if key == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0
        elif key == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0

Game()
arcade.run()