#Save images as Image.html and compress TD tags


class pixel:
    def __init__(self, x, y, rgbColor,hex):
        self.x = x
        self.y = y
        self.rgbColor = rgbColor

    def getRGB(self):
        return self.rgbColor

    def type(self):

        #If there is no color information
        if (self.rgbColor == 0):
            return '*'

        #Adverages out the pixels to be black and white
        inten = int((self.rgbColor[0]+self.rgbColor[1]+self.rgbColor[2])/3)/255*100

        #Gradient detault, (highlights to dark)
        #70:░, 60:▒, 45:▓, 35:█

        #Prints dark areas
        if(inten <= 35):
            return '█'

        #Prints low mid tones
        if (inten <= 45):
            return '▓'

        #Prints high mid tones
        elif(inten <= 60):
            return '▒'

        #Prints highlights
        elif (inten <= 70):
            return '░'

        #Empty space
        else:
            return ' '

        #Keeps the color of each tile

        # Prints dark areas
        # if(inten <= 70):
        #    return "[color=#"+self.hex+']'+'█'+"[/color]"
        ##Empty space
        #else:
        #    return '[color=#2e3b41]'+'█'+"[/color]"


image = open("Image.html", encoding='utf8')

ImageText = image.readlines()

width = 0
height = 0

width = int(input("Width"))
height = int(input("Height"))

width += 1

#Initalizing each pixel objects
pixels = []
for locx in range(width):
    pixels.append([])
    for locy in range(height):
        pixels[locx].append(pixel(locx, locy, 0,0))

#Sets start areas for reading the file
x=1
y=0
i=0
firstPass = False

#Reads the html file and assigns an x, y and an rgb list to each object
print("Reading .html file...")
for i in range(6,len(ImageText)):
    if("R=" in ImageText[i] and y < height-1):
        location = ImageText[i].find("#")
        endLocation = ImageText[i].find(">")
        hexCode = ImageText[i][location+1:endLocation]
        #print(hexCode)
        rgb = tuple(int(hexCode[z:z+2], 16) for z in (0, 2 ,4))
        #print(rgb)

        pixels[x][y].rgbColor = list(rgb)
        pixels[x][y].hex = hexCode

        #print(x, y, pixels[x][y].rgbColor)

        if(x == width-1):
            y += 1
            x = 0
        x += 1

#Writes each character depending on rgb values
line = ""
print("Writing text to a .txt file...")
asciiBird = open("Image.txt",'w+',encoding='utf8')
for y in range(1,height-1):
    for x in range(1,width):
        print(x, y, pixels[x][y].rgbColor)
        line += str(pixels[x][y].type())
    print(line)
    asciiBird.write(line+'\n')
    line = ''

