
lines = [f.strip('\n') for f in open('fb_down_finished.txt', 'r')]


if "001.mp4|https://www.facebook.com/www.upyinnyarnanda/videos/422925304972271/" in list(set(lines)):
    print('yes')
