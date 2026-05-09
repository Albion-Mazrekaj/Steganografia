from  PIL import Image
import random

# 1. CONFIGURATION
key = 12345                 
colourPlane = 0              
significantBit = 7           
coverImage = "img/flowers.bmp"   
secretFile = "secret.txt"    
outputImage = "stego-img.bmp"

# 2. READ THE COVER IMAGE AND SECRET MESSAGE
image = Image.open(coverImage).convert("RGB")
dimensions = image.size
pixels = image.load()

with open(secretFile, "r", encoding="utf-8") as f:
    secret = f.read()

# 3. CHECK IMAGE CAPACITY
total_pixels = dimensions[0] * dimensions[1]

# convert message to 7-bit ASCII
sbits = ''.join(format(ord(char), 'b').zfill(7) for char in secret)

# 14 bits for length
lbits = format(len(secret), 'b').zfill(14)

bits = lbits + sbits

# capacity check
if len(bits) > total_pixels:
    raise ValueError("Image does not have enough capacity!")


# 4. GENERATE THE PIXEL EMBEDDING ORDER
shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)

# 5. HELPER FUNCTION
def modify_pixel(pixel, plane, bit, modifier):
    m = modifier * (2 ** (7 - bit))

    r = pixel[0] + m if plane == 0 else pixel[0]
    g = pixel[1] + m if plane == 1 else pixel[1]
    b = pixel[2] + m if plane == 2 else pixel[2]

    # clamp values to [0,255]
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return (r, g, b)


# 6. EMBED THE SECRET BITS
for i in range(len(bits)):
    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]

    pixel = pixels[x, y]
    value = pixel[colourPlane]

    p = format(value, 'b').zfill(8)

    if p[significantBit] == '0' and bits[i] == '1':
        pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, 1)

    elif p[significantBit] == '1' and bits[i] == '0':
        pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, -1)

# 7. SAVE IMAGE
image.save(outputImage)

print("Embedding complete. Output saved as:", outputImage)