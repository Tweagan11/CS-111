import sys
from byuimage import Image


def load_image(img, red, green, blue):
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            pixel.red = red
            pixel.green = green
            pixel.blue = blue


def detect_green(img, threshold, factor):
    average = (img.red + img.green + img.blue)/3
    if img.green >= average * factor and img.green > threshold:
        return True

def switch_pixel(new_image, old_image, border_width=0, border_height=0, flip_y=1, flip_x=1, factor=1.0, threshold=255):
    if flip_y != 1:
        inv_height = new_image.height - 1
    else:
        inv_height = 0

    if flip_x != 1:
        inv_width = new_image.width - 1
    else:
        inv_width = 0
    for y in range(new_image.height):
        for x in range(new_image.width):
            new_pixel = new_image.get_pixel(x * flip_x + inv_width, (y * flip_y) + inv_height)
            old_pixel = old_image.get_pixel(x + border_width, y + border_height)
            if not detect_green(new_pixel, threshold, factor):
                old_pixel.green = new_pixel.green
                old_pixel.blue = new_pixel.blue
                old_pixel.red = new_pixel.red
    return old_image


def flipped(filename):
    img = Image(filename)
    flipped = Image.blank(img.width, img.height)
    switch_pixel(img, flipped, 0, 0, -1, 1)
    return flipped


def mirror(filename):
    img = Image(filename)
    flipped = Image.blank(img.width, img.height)
    switch_pixel(img, flipped, 0, 0,1,-1)
    return flipped


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


def make_borders(filename, thickness, red, green, blue):
    img = Image(filename)
    thickness = thickness * 2
    border = Image.blank(img.width + thickness, img.height + thickness)
    load_image(border, red, green, blue)
    switch_pixel(img, border, thickness//2, thickness//2)
    return border


def collage(file1, file2, file3, file4, thickness):
    img1 = Image(file1)
    img2 = Image(file2)
    img3 = Image(file3)
    img4 = Image(file4)
    background = Image.blank(img1.width + img2.width + (3 * thickness), img1.height + img2.height + (3 * thickness))
    load_image(background, 0,0,0)
    switch_pixel(img1, background, thickness, thickness)
    switch_pixel(img2, background, (2 * thickness) + img1.width, thickness)
    switch_pixel(img3, background, thickness, (2*thickness) + img1.height)
    switch_pixel(img4, background, (2 * thickness) + img1.width, (2 * thickness) + img1.height)
    return background


def green_screen(over_file, under_file, threshold, factor):
    over_img = Image(over_file)
    under_img = Image(under_file)
    switch_pixel(over_img, under_img, 0,0,1,1, float(factor), int(threshold))
    return under_img


def validate_commands(lst):
    if lst[1] == "-d" and len(lst) > 2:
        img = Image(lst[2])
        img.show()
        return True
    elif lst[1] == "-k" and len(lst) > 4:
        percent = float(lst[4])
        darken(lst[2], percent).save(lst[3])
        return True
    elif lst[1] == "-s" and len(lst) > 3:
        sepia(lst[2]).save(lst[3])
    elif lst[1] == "-g" and len(lst) > 3:
        grayscale(lst[2]).save(lst[3])
    elif lst[1] == "-b" and len(lst) > 6:
        thickness = int(lst[4])
        make_borders(lst[2], thickness, lst[5], lst[6], lst[7]).save(lst[3])
    elif lst[1] == "-f" and len(lst) > 3:
        flipped(lst[2]).save(lst[3])
    elif lst[1] == "-m" and len(lst) > 3:
        mirror(lst[2]).save(lst[3])
    elif lst[1] == "-c" and len(lst) > 7:
        thickness = int(lst[7])
        collage(lst[2], lst[3], lst[4], lst[5], thickness).save(lst[6])
    elif lst[1] == "-y" and len(lst) > 6:
        green_screen(lst[2], lst[3], lst[5], lst[6]).save(lst[4])
    else:
        return False


if __name__ == "__main__":
    validate_commands(sys.argv)
