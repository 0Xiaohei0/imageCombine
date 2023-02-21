from PIL import Image
import os
import rpack


def merge(imageArray, positionArray, size):
    output = Image.new("RGBA", size)
    for idx, image in enumerate(imageArray):
        output.paste(image, positionArray[idx])
    return output


scale = False
maxsize = (200, 200)
resizeFactor = 0.1
path = "../images"
fileNames = os.listdir(path)
imageArray = []

print("Loading image...")
for idx, name in enumerate(fileNames):
    image = Image.open(path + "/" + name)
    print("Resizing ", end="")
    print(idx + 1, end="")
    print(" out of ", end="")
    print(len(fileNames))
    if scale:
        image = image.resize(
            (
                (int(float(image.size[0]) * resizeFactor)),
                (int(float(image.size[1]) * resizeFactor)),
            )
        )
    else:
        image.thumbnail(maxsize, Image.ANTIALIAS)
    imageArray.append(image)

print("Packing...")
sizeArray = list(map(lambda image: (image.size[0], image.size[1]), imageArray))
positionArray = rpack.pack(sizeArray)

print("Packing finished with size: ", rpack.bbox_size(sizeArray, positionArray))

mergedImage = merge(
    imageArray, positionArray, rpack.bbox_size(sizeArray, positionArray)
)
mergedImage.save("output.png")
mergedImage.show()
