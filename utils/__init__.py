from PIL import Image

def rgb2hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def ConvertImageToPixels(path,pixelsize,threshold):
    input_image = Image.open(path)
    new_image = Image.new("RGBA", input_image.size, "WHITE")
    new_image.paste(input_image, (0, 0), input_image) 
    new_image.convert('RGB')
    pixel_map = new_image.load()
    pixels = {
        'color':[],
        'gray':[],
        'binary':[]
    }

    width, height = new_image.size

    for i in range(int(height/pixelsize)+1):
        pixels['color'].append([])
        pixels['gray'].append([])
        pixels['binary'].append([])
        for j in range(int(width/pixelsize)+1):
            r, g, b, p = new_image.getpixel((j*pixelsize, i*pixelsize))
            grayscale = (0.299*r + 0.587*g + 0.114*b)

            pixels['color'][i].append('%s' % (rgb2hex(r, g, b)))
            pixels['gray'][i].append(grayscale)
            pixels['binary'][i].append('1' if grayscale <= threshold else "0")


    return pixels


def PixelsToText(pixels):
    text_output = ''
    for x in pixels['binary']:
        text_output+='\n'
        for y in x:
            text_output+=y

    return text_output

def CalculateClues(binary):
    rowClues = []
    colClues = []

    for c in binary:
        cons = []
        consN = 0
        for idx, r in enumerate(c):
            if r == '0' and c[idx-1] == '1' and consN > 0:
                cons.append(consN)
                consN = 0
            elif r == '1':
                consN += 1

        rowClues.append(cons)

    print(rowClues)
