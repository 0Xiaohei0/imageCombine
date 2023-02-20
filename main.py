from PIL import Image
import os
import rpack


def merge(imageArray):
    w = 0
    maxh = 0
    for image in imageArray:
        w += image.size[0]
        maxh = max(image.size[1], maxh)
    output = Image.new("RGBA", (w, maxh))

    pasteStart = 0
    for image in imageArray:
        output.paste(image, (pasteStart, 0))
        pasteStart += image.size[0]

    return output


path = "../images"
fileNames = os.listdir(path)
imageArray = []
for name in fileNames:
    imageArray.append(Image.open(path + "/" + name))


sizeArray = map(lambda image: (image.size[0], image.size[1]), imageArray)
positions = rpack.pack(sizeArray)
print(positions)

mergedImage = merge(imageArray)
mergedImage.show()
