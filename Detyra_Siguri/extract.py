from PIL import Image
import random

# Çelësi për randomizim (duhet të jetë i njëjtë si në embed)
key = 12345

# Zgjedh kanalin e ngjyrës (0 = Red, 1 = Green, 2 = Blue)
colourPlane = 0

# Biti që është përdorur për fshehje (LSB ose bit specifik)
significantBit = 7

# Emri i imazhit të steganografuar
stegoImage = "stego-img.bmp"

# Hap imazhin dhe e konverton në RGB format
image = Image.open(stegoImage).convert("RGB")

# Merr dimensionet e imazhit (gjerësia, lartësia)
dimensions = image.size

# Merr akses në pikselat e imazhit
pixels = image.load()

# Numri total i pikselave në imazh
total_pixels = dimensions[0] * dimensions[1]

# Krijon listë me indekset e pikselave
shuffledIndices = list(range(total_pixels))

# Përzien indeksat në mënyrë të rastësishme me seed (çelës)
random.seed(key)
random.shuffle(shuffledIndices)

# Këtu do ruhen bitët e nxjerrë nga imazhi
extractedBits = []

# Nxjerr bitin e fshehur nga çdo pixel sipas rendit të përzier
for i in shuffledIndices:
    x = i % dimensions[0]   # koordinata X
    y = i // dimensions[0]  # koordinata Y

    # Merr vlerën e ngjyrës dhe e kthen në binar (8-bit)
    p = format(pixels[x, y][colourPlane], '08b')

    # Merr bitin e fshehur (LSB ose bit i zgjedhur)
    extractedBits.append(p[significantBit])

# Nxjerr gjatësinë e mesazhit (14 bitët e parë)
extractedLength = int(''.join(extractedBits[:14]), 2)

# String për mesazhin e rikuperuar
secret = ''

# Rikonstrukton mesazhin karakter për karakter
for i in range(extractedLength):
    # Merr 7 bitët për çdo karakter
    char_bits = extractedBits[14 + i*7 : 14 + (i+1)*7]

    # Kthen binarin në numër
    value = int(''.join(char_bits), 2)

    # Kthen numrin në karakter ASCII
    secret += chr(value)

# Shfaq mesazhin e fshehur
print("Recovered message:")
print(secret)
