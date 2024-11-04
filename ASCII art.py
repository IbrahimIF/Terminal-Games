from PIL import Image
im = Image.open("Untitled.jpg")

print(im.format)


arra = im.load()
print(arra)



#for x in len(pixel_matrix):
    #for y in len(pixel_matrix[x]):
        #pixel = pixel_matrix[x][y]
        # Now do something with the pixel...
#below is a qucik revised version of the above
pixels = list(im.getdata())

pixel_matrix = [pixels[i:i + im.width] for i in range(0, len(pixels), im.width)]
# print(pixel_matrix)

brightness_matrix = []
ASCII_matrix = []
for r in pixel_matrix:
    brightness_row = []
    ASCII_row = []
    for (r, b, g) in r:
        mavs =(r + b + g) / 3 # average to get brightness for each pixel
        brightness_row.append(mavs) # if statment is going up in 25.5 
        if mavs == 0:  
            ASCII_row.append("^")
        elif mavs <= 25.5:
            ASCII_row.append(":")
        elif mavs <= 76.5:
            ASCII_row.append("~")
        elif mavs <= 102:
            ASCII_row.append("|")
        elif mavs <= 127.5:
            ASCII_row.append("x")
        elif mavs <= 153:
            ASCII_row.append("L")
        elif mavs <= 178.5:
            ASCII_row.append("m")
        elif mavs <= 204:
            ASCII_row.append("#")
        elif mavs <= 229.5:
            ASCII_row.append("8")
        else:
            ASCII_row.append("B")

    brightness_matrix.append(brightness_row)
    ASCII_matrix.append(ASCII_row)



for row in ASCII_matrix:
    print("".join(row))

