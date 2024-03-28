from byuimage import Image

def flipped(filename):
    img = Image(filename)
    flipped = Image.blank(img.width, img.height)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, img.height - y - 1)
            flipped_pixel = flipped.get_pixel(x, y)
            flipped_pixel.red = pixel.red
            flipped_pixel.green = pixel.green
            flipped_pixel.blue = pixel.blue
    return flipped

def make_borders(filename, thickness, red, green, blue):
    img = Image(filename)
    thickness = thickness * 2
    border = Image.blank(img.width + thickness, img.height + thickness)
    for y in range(border.height):
        for x in range(border.width):
            pixel = border.get_pixel(x,y)
            pixel.red = red
            pixel.green = green
            pixel.blue = blue

    for y in range(img.height):
        for x in range(img.width):
            old_pixel = img.get_pixel(x,y)
            new_pixel = border.get_pixel(x + thickness//2,y + thickness//2)
            new_pixel.red = old_pixel.red
            new_pixel.green = old_pixel.green
            new_pixel.blue = old_pixel.blue
    return border



if __name__ == "__main__":
    pass


make_borders('test_files/landscape.png', 10, 255,125,125).show()
