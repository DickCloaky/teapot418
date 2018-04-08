# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time

#import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
#RJH I don't use SPI?
DC = 23
#SPI_PORT = 0
#SPI_DEVICE = 0

# 128x64 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)

disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

#font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype('Mario-Kart-DS.ttf', 16)

timg = Image.open('teapot_image.png').resize((disp.width, disp.height), Image.ANTIALIAS).convert('1')
while True:
	disp.image(timg)
	disp.display()
	time.sleep(3)
	for msg in (
		'Hello\nJudges!',
		'Fancy a\nhobnob?',
		'I am\nteapot418',
		'How do you\nlike your\ntea?',
		'One lump\nor two?',
		'Thank you\nso much for\nhelping out!',
		'I hope you\nare enjoying\nthe\ncompetition',
		'They say\nflattery\nwill get you\neverywhere...',
		'You guys are\nlooking\nfabulous\ntoday!',
	):
		x = 5
		y = 5
		draw.rectangle((0,0,width,height), outline=0, fill=0)
		for line in msg.splitlines():
			draw.text((x, y), line.upper(), font=font, fill=255)
			y += 15
	
# Display image.
		disp.image(image)
		disp.display()
		time.sleep(3)
