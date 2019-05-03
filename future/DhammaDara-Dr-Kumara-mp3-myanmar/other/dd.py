from PIL import Image, ImageDraw, ImageFont
#variables for image size

#img = Image.open("photo-001.jpg")
#img = Image.open("photo-004.jpg")
img = Image.open("photo-003.jpg")
#img = Image.open("photo-002.jpg")


#width, height = img.size
width, height = img.size
x1, y1 = img.size
height = y1
print('width', x1)
print('height', y1)
print('hello', y1//2 + (y1 + 350))
y1 = y1//2 + (y1 + 350)
yy = y1//2 + 50
print(yy)
#x1 = 612
#y1 = 612
#my quote
#sentence = "Everybody is a genius. But if you judge a fish by its ability to climb a tree, it will live its whole life believing that it is stupid. -Albert Einstein"
#sentence = "၁။ လူငယ္တို႔ အ ေမး ယ ေန႔ေခတ္ဘာသာေရး"
sentence = "၃။ ကွက်လပ်ကိုသာ ဖြည့်ပေးပါ "
#sentence = "Hello world from images"
#choose a font
fnt = ImageFont.truetype('Myanmar3.ttf', 30)
#img = Image.new('photo-001.jpg', (x1, y1), color = (255, 255, 255))
d = ImageDraw.Draw(img)
#find the average size of the letter
sum = 0
for letter in sentence:
    print(letter)
    sum += d.textsize(letter, font=fnt)[0]
average_length_of_letter = sum/len(sentence)
print(average_length_of_letter)
#find the number of letters to be put on each line
number_of_letters_for_each_line = (x1/1.618)/average_length_of_letter
incrementer = 0
fresh_sentence = ''
#add some line breaks
for letter in sentence.strip():
  if(letter == '-'):
    fresh_sentence += '\n\n' + letter
  elif(incrementer < number_of_letters_for_each_line):
    fresh_sentence += letter
  else:
    if(letter == ' '):
      #fresh_sentence += '\n'
      fresh_sentence += ' '
      incrementer = 0
    else:
      fresh_sentence += letter
  incrementer+=1
  #print(fresh_sentence)
#render the text in the center of the box
#dim = d.textsize(fresh_sentence, font=fnt)
dim = d.textsize(sentence, font=fnt)
x2 = dim[0]
y2 = dim[1]
qx = (x1/2 - x2/2)
qy = (y1/2-y2/2)

print('x2', x2)
print('y2', y2)
print('qx', qx)
print('qy', qy)

#d.rectangle((70, 50, 270, 200), outline='red', fill='blue')
#print('qz', qx)
#print('qy', qy)
#d.rectangle((70, 50, 270, 200), outline='red', fill='blue')

#d.rectangle((right, top-down, width, height), outline='red', fill='blue')
#d.rectangle((0, y1, x1, int(qy)), outline='red', fill='blue')
#d.rectangle((0, 850, x1, 950), outline='red', fill='blue')

#d.rectangle((0, qy, x1, (height - 50)), outline='red', fill='blue')
#d.text((qx,qy), fresh_sentence ,align="center",  font=fnt, fill=(100,100,100))
#img.save('quote1.png')


x, y = (width-200, height-100)
#xx, yy = (width-400, height-100)
#w, h = d.textsize(sentence, font=fnt)
#d.rectangle((0, y, x + w, y + h + 50), fill='green')
d.text((qx,y+30), fresh_sentence, align="center",fill='white', font=fnt)
#img.save('quote4.png')
#img.save('quote3.png')
img.save('quote33333.png')
