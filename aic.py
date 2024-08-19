from PIL import Image


def get_median_color(path):
    target_image = Image.open(path)
    width, height = target_image.size
    total_pixels = width * height

    red, green, blue = 0, 0, 0

    for w in range(width):
        for h in range(height):
            current_pixel = target_image.crop((w, h, w+1, h+1))

            red += current_pixel.getpixel((0, 0))[0]
            green += current_pixel.getpixel((0, 0))[1]
            blue += current_pixel.getpixel((0, 0))[2]

    red = round(red/total_pixels)
    green = round(green/total_pixels)
    blue = round(blue/total_pixels)

    return red, green, blue
