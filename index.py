from PIL import Image
from os import walk

sourcePath = "C:/Users/joshu/Documents/rpg citymap generator/stonewall options/2/"
imageSize = 3200
matrixSize = 7
canvasSize = imageSize * matrixSize

def main():
    canvas = Image.new("RGBA", (canvasSize, canvasSize))
    fileNames = []
    # Load names of images
    for (_, __, filenames) in walk(sourcePath):
        fileNames.extend(filenames)
        break
    # Put everything into place
    for index in range(0, len(fileNames)):
        # Load image
        image = Image.open(sourcePath + fileNames[index])
        # Get it's position in the end result
        position = getPosition(fileNames[index])
        # Paste it into position
        canvas.paste(image, (position[1], position[0]))
    canvas.save('output.png')
    print('saved output')

def getPosition(name):
    # name is in the format of something_01_02
    # separate to [something, 01, 02]
    yposition = name.split("_")[1]
    # separate 01 to just 1
    if yposition[0] == '0':
        yposition = yposition[1]
    xposition = name.split("_")[2]
    # separate 02 to just 2
    if xposition[0] == '0':
        xposition = xposition[1]
    # convert to coordinates
    ycoordinate = (int(yposition) - 1) * imageSize
    xcoordinate = (int(xposition) - 1) * imageSize
    return [xcoordinate, ycoordinate]


# Begin the program
main()