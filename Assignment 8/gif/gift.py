import os
import imageio

images=[]
file = os.listdir("image")
for i in range(len(file)):
    img= imageio.imread("image/"+file[i])
    images.append(img)

imageio.mimsave("img.gif",images)