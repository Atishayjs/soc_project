# create a thumbnail of an image
from PIL import Image
# load the image
image = Image.open('opera_house.jpg')
# report the size of the image
print(image.size)
# create a thumbnail and preserve aspect ratio
i=image.resize((690,790))
# report the size of the thumbnail
print(i.size)
i.show()
