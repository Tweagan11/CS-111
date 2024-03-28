# IMPORTANT - Remember to import Image from the byuimage library: `from byuimage import Image`
from byuimage import Image

def bottom(img):
    new_image = img.copy(img.height + 50, img.width)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.getpixel(x, y)
            new_pixel = new_image.getpixel(x, y)
            new_pixel.blue = pixel.blue
            new_pixel.green = pixel.green
            new_pixel.red = pixel.red
            new_image.putpixel((x, y), new_pixel)


def iron_puzzle(filename):
    img = Image(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.blue = pixel.blue * 10
            pixel.green = 0
            pixel.red = 0
    return img


def west_puzzle(filename):
    img = Image(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.green = 0
            pixel.red = 0
            if pixel.blue < 16:
                pixel.blue *= 16
            else:
                pixel.blue = 0
    return img

west_puzzle("test_files/west.png")

def darken(filename, percent):
    img = Image(filename)
    percent = 1 - percent
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.blue *= percent
            pixel.green *= percent
            pixel.red *= percent
    return img



def grayscale(filename):
    img = Image(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            average = (pixel.red + pixel.green + pixel.blue) / 3
            pixel.blue = average
            pixel.green = average
            pixel.red = average
    return img

def sepia(filename):
    img = Image(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            true_red = 0.393 * pixel.red + 0.769 * pixel.green + 0.189 * pixel.blue
            true_green = 0.349 * pixel.red + 0.686 * pixel.green + 0.168 * pixel.blue
            true_blue = 0.272 * pixel.red + 0.534 * pixel.green + 0.131 * pixel.blue
            pixel.blue = true_blue
            pixel.red = true_red
            pixel.green = true_green
            if pixel.blue > 255:
                pixel.blue = 255
            if pixel.green > 255:
                pixel.green = 255
            if pixel.red > 255:
                pixel.red = 255
    return img

def create_left_border(filename, weight):
    img = Image(filename)
    border = Image.blank(img.width+weight, img.height)
    for y in range(border.height):
        for x in range(0,weight):
            pixel = border.get_pixel(x, y)
            pixel.blue = 255
            pixel.red = 0
            pixel.green = 0
    for y in range(border.height):
        for x in range(weight,border.width):
            old_pixel = img.get_pixel(x-weight,y)
            new_pixel = border.get_pixel(x,y)
            new_pixel.blue = old_pixel.blue
            new_pixel.green = old_pixel.green
            new_pixel.red = old_pixel.red
    return border


###################################################
# Code below here is for extra practice and doesn't count for or against
# your grade on this lab.
def create_stripes(filename):
    img = Image(filename)
    stripes = Image.blank(img.width+50, img.height+25)
    for y in range(stripes.height):
        for x in range(stripes.width):
            pixel = stripes.get_pixel(x, y)
            if (y % 2 == 0):
                pixel.green = 255
                pixel.blue = 0
                pixel.red = 0
            elif (x % 2 == 1):
                pixel.green = 0
                pixel.blue = 255
                pixel.red = 0
            else:
                pixel.green = 0
                pixel.blue = 0
                pixel.red = 255

    return stripes

create_stripes("test_files/cougar.png").show()

def copper_puzzle(filename):
    img = Image(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.blue *= 20
            pixel.green *= 20
            pixel.red = 0
    return img