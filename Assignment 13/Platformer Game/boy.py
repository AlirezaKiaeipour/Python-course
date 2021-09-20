import arcade
from arcade.key import S

class Boy(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()

        self.stand_right_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png")]
        self.stand_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png",mirrored=True)]

        self.walk_right_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png"),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png")]

        self.walk_left_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk0.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk1.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk2.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk3.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk4.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk5.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk6.png",mirrored=True),
                                    arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_walk7.png",mirrored=True)]

        self.walk_up_textures = [arcade.load_texture(":resources:images/animated_characters/male_adventurer/maleAdventurer_jump.png")]

        self.width = 80
        self.height = 80
        self.center_x = 120
        self.center_y = 300
        self.speed = 3
        self.health = 120
        self.pocket_list = [] 