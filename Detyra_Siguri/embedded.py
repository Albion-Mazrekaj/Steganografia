from PIL import Image
import random

# 1. KONFIGURIMI I SISTEMIT
# Çelësi për randomizimin e pikselave (duhet të jetë i njëjtë në extract)
key = 2026

# Kanali i ngjyrës që do përdoret (0=Red, 1=Green, 2=Blue)
colourPlane = 0

# Biti specifik ku do fshihet informacioni (LSB ose bit i zgjedhur)
significantBit = 7

# Imazhi bazë (cover image)
coverImage = "Detyra_Siguri/img/flowers.bmp"

# File që përmban mesazhin sekret
secretFile = "Detyra_Siguri/secret.txt"

# Imazhi i output-it me mesazhin e fshehur
outputImage = "Detyra_Siguri/stego-img.bmp"


# 2. LEXIMI I TË DHËNAVE
image = Image.open(coverImage).convert("RGB")
dimensions = image.size
pixels = image.load()

with open(secretFile, "r", encoding="utf-8") as f:
    secret = f.read()

# 3. PËRGATITJA E MESAZHIT
# Numri total i pikselave
total_pixels = dimensions[0] * dimensions[1]

# Mesazhi në 7-bit ASCII
sbits = ''.join(format(ord(char), '07b') for char in secret)

# 14-bit header për gjatësinë
lbits = format(len(secret), '014b')

bits = lbits + sbits

# Kontroll kapaciteti
if len(bits) > total_pixels:
    raise ValueError("Image does not have enough capacity!")


# 4. RANDOMIZIMI I PIKSELAVE
shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)


# 5. FSHEHJA E MESAZHIT
for i in range(len(bits)):

    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]

    pixel = list(pixels[x, y])
    value = pixel[colourPlane]

    # vendos 0 në bitin e zgjedhur
    value = value & ~(1 << significantBit)

    # vendos bitin e mesazhit
    value = value | (int(bits[i]) << significantBit)

    pixel[colourPlane] = value
    pixels[x, y] = tuple(pixel)


# 6. RUAJTJA E IMAZHIT FINAL
image.save(outputImage)

print("Embedding complete. Output saved as:", outputImage)
