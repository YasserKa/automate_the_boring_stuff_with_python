from PIL import Image
from PIL import ImageDraw

LOGO_FILENAME = 'flower.jpeg'
logoIm = Image.open(LOGO_FILENAME)
logoIm.resize((50, 50))


def drawAnInvitation(name):
    im = Image.new('RGBA', (288, 360), 'white')
    im.paste(logoIm, (0, 0))
    draw = ImageDraw.Draw(im)
    draw.text((20, 150), name, fill='black')
    im.save(name.strip() + ' invitation.png')
    pass


guests = open('guests.txt', 'r')

# for each guest create a drawing
for guest in guests:
    drawAnInvitation(guest)
