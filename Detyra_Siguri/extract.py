from PIL import Image
import random

# 1. KONFIGURIMI I SISTEMIT
# Çelësi për randomizimin e pikselave 
key = 2026

# Kanali i ngjyrës që është përdorur (0=Red, 1=Green, 2=Blue)
colourPlane = 0

# Biti specifik ku është fshehur informacioni
significantBit = 7

# Imazhi i steganografuar
stegoImage = "Detyra_Siguri/stego-img.bmp"


# 2. LEXIMI I IMAZHIT
image = Image.open(stegoImage).convert("RGB")
dimensions = image.size
pixels = image.load()

total_pixels = dimensions[0] * dimensions[1]


# 3. RIKRIJIMI I RENDIT TË PIKSELAVE
shuffledIndices = list(range(total_pixels))
random.seed(key)
random.shuffle(shuffledIndices)


# 4. NXJERRJA E BIT-AVE
extractedBits = []

for i in shuffledIndices:

    x = i % dimensions[0]
    y = i // dimensions[0]

    pixel = pixels[x, y]
    value = pixel[colourPlane]

    # nxjerr bitin e zgjedhur (LSB)
    bit = (value >> significantBit) & 1
    extractedBits.append(str(bit))


# 5. NXJERRJA E GJATËSISË SË MESAZHIT
length_bits = ''.join(extractedBits[:14])
message_length = int(length_bits, 2)


# 6. RIKONSTRUKTIMI I MESAZHIT
secret = ""

for i in range(message_length):
    char_bits = extractedBits[14 + i*7 : 14 + (i+1)*7]
    value = int(''.join(char_bits), 2)
    secret += chr(value)

# 7. OUTPUT
print("Recovered message:")
print(secret)
