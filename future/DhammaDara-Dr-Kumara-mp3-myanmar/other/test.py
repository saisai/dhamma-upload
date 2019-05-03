'''
from PIL import Image, ImageFont, ImageDraw
im = Image.open("photo-001.jpg")
helvetica = ImageFont.truetype("zawgyi.ttf", 30)
d = ImageDraw.Draw(im)

location = (50, 850)
text_color = (100, 100, 200)
#d.text(location, "၁။ လူငယ္တို႔အေမး ယေန႔ေခတ္ဘာသာေရး", font=helvetica, fill=text_color)
im.rectangle((x, y, x + w, y + h), fill='black')
d.text(location, "၁။ လူငယ္တို႔ အ ေမး ယ ေန႔ေခတ္ဘာသာေရး", font=helvetica, fill=text_color)
im.save("drawn_grid_2.jpg")
'''

#import Image
#import ImageFont
#import ImageDraw

from PIL import Image, ImageFont, ImageDraw

img = Image.open("photo-001.jpg")


width, height = img.size

draw = ImageDraw.Draw(img)
font = ImageFont.truetype(
    "zawgyi.ttf", 30)
#x, y = (width - 510, height-100)
x, y = width, height - 100
# x, y = 10, 10
text = "၁။ လူငယ္တို႔ အ ေမး ယ ေန႔ေခတ္ဘာသာေရး"
w, h = font.getsize(text)
draw.rectangle((x, y, x + w, y + h), fill='black')
draw.text((x, y), text, fill=(209, 239, 8), font=font)
img.save('out.jpg')