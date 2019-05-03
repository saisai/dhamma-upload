from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
 
def text_wrap(text, font, max_width):
    lines = []
    # If the width of the text is smaller than image width
    # we don't need to split it, just add it to the lines array
    # and return
    if font.getsize(text)[0] <= max_width:
        lines.append(text) 
    else:
        # split the line by spaces to get words
        words = text.split(' ')  
        i = 0
        # append every word to a line while its width is shorter than image width
        while i < len(words):
            line = ''         
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:                
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            # when the line gets longer than the max width do not append the word, 
            # add the line to the lines array
            lines.append(line)    
    return lines
 
 
def draw_text(text):    
    # open the background file
    img = Image.open('photo-001.jpg')
    
    # size() returns a tuple of (width, height) 
    image_size = img.size 
 
    # create the ImageFont instance
    font_file_path = 'zawgyi.ttf'
    font = ImageFont.truetype(font_file_path, size=30, encoding="unic")
 
    # get shorter lines
    lines = text_wrap(text, font, image_size[0])
    print(lines) # ['This could be a single line text ', 'but its too long to fit in one. ']
    line_height = font.getsize('hg')[1]
    
    x = 10
    y = 20
    draw = ImageDraw.Draw(img)
    for line in lines:
        # draw the line on the image
        #draw.text((x, y), line, fill=color, font=font)
        #draw.text((x, y), line, fill=(209, 239, 8), font=font)
        #draw.multiline_text((x, y), line, fill=(209, 239, 8), font=font, align='center')
        draw.multiline_text((0, 0), line, fill=(209, 239, 8), font=font, align='center')
        
        # update the y position so that we can use it for next line
        y = y + line_height
    # save the image
    img.save('word2.jpg', optimize=True)    
 
 
if __name__ == '__main__':
    draw_text("၁။ လူငယ္တို႔ အ ေမး ယ ေန႔ေခတ္ဘာသာေရး")
    #draw_text("This could be a single line text but its too long to fit in one.")
    #text = "This could be a single line text but its too long to fit in one."
    #lines = text_wrap(text, font, image_size[0])
    
    
    '''
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
    '''
