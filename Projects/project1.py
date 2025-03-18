###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("arcticmountains")

q1 = codesters.Square(100, 100, 200, 'CornflowerBlue')
q2 = codesters.Square(-100, 100, 200, 'LightPink')
q3 = codesters.Square(-100, -100, 200, 'GreenYellow')
q4 = codesters.Square(100, -100, 200, 'LightSalmon')

s1 = codesters.Sprite("Penguin2", 60, 100)
s1.set_size(0.3)
s2 = codesters.Sprite("pinkflower", -100, -100)
s2.set_size(0.4)
s3 = codesters.Sprite("bookstack", 100, -100)
s3.set_size(0.3)
s4 = codesters.Sprite("kitten", -100, 100)
s4.set_size(1.5)

message1 = codesters.Text("Ayame Daina Stevens", 0, 220, "RosyBrown")
message2 = codesters.Text("I am cool", 0, -220, "Orchid")