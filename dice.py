import math
from PIL import Image
scale = 255

dices = []
dices_count = {}
dice_size = 100
for i in range(1, 7):
    img_path = "./dices-img/dices-black/dice-" + str(i) + ".png"
    dice_img = Image.open(img_path);
    dice_img = dice_img.resize((dice_size, dice_size), resample=Image.BILINEAR)
    dices.append(dice_img)
    dices_count[i] = 0;

img_size = 50
img = Image.open("./marlin.jpeg")
# img = img.convert("L")
img = img.resize((img_size, img_size), resample=Image.BILINEAR).load()

img_result = Image.new(mode="RGB", size = (img_size*dice_size, img_size*dice_size), color = 0)

for x in range (0, img_size):
    for y in range (0, img_size):
        pixel_dice = math.ceil((img[x, y][0] * 5 / 255))
        Image.Image.paste(img_result, dices[pixel_dice], (x*100, y*100))

# Save
img_result.save('result.png')
