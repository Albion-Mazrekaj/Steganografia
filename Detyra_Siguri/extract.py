from PIL import Image
import random

key = 12345
colourPlane = 0

significantBit = 7

stegoImage = "stego-img.bmp"

image = Image.open(stegoImage).convert("RGB")
dimensions = image.size
pixels = image.load()

total_pixels = dimensions[0] * dimensions[1]

shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)

extractedBits = []

for i in shuffledIndices:
    x = i % dimensions[0]
    y = i // dimensions[0]

    p = format(pixels[x, y][colourPlane], '08b')
    extractedBits.append(p[significantBit])

extractedLength = int(''.join(extractedBits[:14]), 2)

secret = ''

for i in range(extractedLength):
    char_bits = extractedBits[14 + i*7 : 14 + (i+1)*7]
    value = int(''.join(char_bits), 2)
    secret += chr(value)

print("Recovered message:")
print(secret)