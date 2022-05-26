# # create flipped versions of an image
# from PIL import Image
# from matplotlib import pyplot
# # load image
# image = Image.open('opera_house.jpg')
# # horizontal flip
# hoz_flip = image.transpose(Image.FLIP_LEFT_RIGHT)
# # vertical flip
# ver_flip = image.transpose(Image.FLIP_TOP_BOTTOM)
# # plot all three images using matplotlib
# pyplot.subplot(311)
# pyplot.imshow(image)
# pyplot.subplot(312)
# pyplot.imshow(hoz_flip)
# pyplot.subplot(313)
# pyplot.imshow(ver_flip)
# pyplot.show()

# # create rotated versions of an image
# from PIL import Image
# from matplotlib import pyplot
# # load image
# image = Image.open('cjs.jpg')
# # plot original image
# pyplot.subplot(311)
# pyplot.imshow(image)
# # rotate 45 degrees
# pyplot.subplot(312)
# pyplot.imshow(image.rotate(42))
# # rotate 90 degrees
# pyplot.subplot(313)
# pyplot.imshow(image.rotate(69))
# pyplot.show()

# example of cropping an image
from PIL import Image
# load image
image = Image.open('mia.jpg')
# create a cropped image
cropped = image.crop((0, 400, 600, 900))
# show cropped image
cropped.show()