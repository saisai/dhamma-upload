from PIL import Image, ImageFont, ImageDraw
im = Image.open("photo-001.jpg")
helvetica = ImageFont.truetype(filename="zawgyi.ttf", size=40)
d = ImageDraw.Draw(im)

location = (100, 50)
text_color = (100, 100, 200)
d.text(location, "၁။ လူငယ္တို႔အေမး ယေန႔ေခတ္ဘာသာေရး", font=helvetica, fill=text_color)

im.save("drawn_grid.jpg")