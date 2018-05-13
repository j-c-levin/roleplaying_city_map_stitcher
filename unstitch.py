from PIL import Image
from os import walk

sourcePath = "C:/Users/joshu/Pictures/rpg/stitched/output-edited.png"
destinationPath = "C:/Users/joshu/Pictures/rpg/unstitched/"
imageSize = 3200
matrixSize = 4

def main():
    # Load in main image
    full_image = Image.open(sourcePath)
    # Create a new canvas
    canvas = Image.new("RGBA", (imageSize, imageSize))
    # Loop through and unstitch
    for x_index in range(0, matrixSize):
        for y_index in range(0, matrixSize):
            # Copy the selected area from the main image
            section = full_image.crop(getCropCoordinates(x_index, y_index))
            # Paste on top of the canvas
            canvas.paste(section, (0,0))
            # Print out the set
            canvas.save(destinationPath + "stitched_0" + str(x_index + 1) + "_0" + str(y_index + 1) + ".png")
            print('saved ' + str(x_index) + " : " + str(y_index))

def getCropCoordinates(x_index, y_index):
    left = x_index * imageSize
    upper = y_index * imageSize
    right = left + imageSize
    lower = upper + imageSize
    return (left, upper, right, lower)

# Begin the program
main()