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

    # Row Clues
    for i,c in enumerate(binary):
        rcons = []
        rconsN = 0
        ri = False

        for idxr, r in enumerate(c):
            if ri and (idxr == len(c)-1) or (r == '0' and rconsN > 0):
                rcons.append(rconsN)
                rconsN = 0
                ri = False
            elif r == '1':
                ri = True
                rconsN += 1

        rowClues.append(' '.join(str(x) for x in rcons))

    # Col Clues
    for j in range(len(binary[0])):
        ccons = []
        cconsN = 0
        ci = False

        for i in range(len(binary)):
            r = binary[i][j]

            if r == '1' and i == len(binary)-1:
                cconsN += 1
                ccons.append(cconsN)
                ci = False
            elif ci and r == '0' and cconsN > 0:
                ccons.append(cconsN)
                cconsN = 0
                ci = False
            elif r == '1':
                cconsN += 1
                ci = True

        colClues.append('\n'.join(str(x) for x in ccons))

    return {'cols':colClues,'rows':rowClues}