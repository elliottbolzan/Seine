import Image, random

n = int(raw_input("Enter the number of 'Seine' imitations you want to create: ") or "1")
width = int(raw_input("Enter the width of the output image: ") or "3000")

xScale = 81
yScale = 41

realWidth = 115

factor = width / xScale

backgroundColor = (220, 205, 170)
pixelColor = (15, 15, 15)

for imitation in xrange(1, n + 1):

    img = Image.new('RGB', (realWidth * factor, yScale * factor), backgroundColor)
    pixels = img.load()

    picked = []
    column = 0
    for i in range(img.size[0] - factor):
        currentColumn = (i / factor) * xScale / realWidth
        if currentColumn > yScale:
            currentColumn = xScale - currentColumn + 1
        if currentColumn != column:
            column = currentColumn
            picked = random.sample(xrange(0, yScale), column)
        for pick in picked:
            for height in xrange(factor):
                pixels[i, factor * pick + height] = pixelColor

    img.save(str(imitation) + ".png", "PNG")