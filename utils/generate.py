from PIL import Image

input_image = Image.open("./test_images/bowser.png")
pixelsize = 25
threshold = 200

new_image = Image.new("RGBA", input_image.size, "WHITE")
new_image.paste(input_image, (0, 0), input_image) 
new_image.convert('RGB')
pixel_map = new_image.load()
pixels = []

width, height = new_image.size

for i in range(int(height/pixelsize)+1):
    pixels.append([])
    for j in range(int(width/pixelsize)+1):
        r, g, b, p = new_image.getpixel((j*pixelsize, i*pixelsize))
        grayscale = (0.299*r + 0.587*g + 0.114*b)

        pixels[i].append(grayscale)

        for k in range(pixelsize):
            for l in range(pixelsize-1):
                pixel_map[((j-1)*pixelsize)+k, ((i-1)*pixelsize)+l] = (int(grayscale), int(grayscale), int(grayscale))

text_output = ''
for x in pixels:
    text_output+='\n'
    for y in x:
        if y >= threshold:
            text_output+=' '
        else:
            text_output+='X'

print(text_output)