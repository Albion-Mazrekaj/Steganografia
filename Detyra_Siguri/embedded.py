from PIL import Image
import random

# 1. KONFIGURIMI I SISTEMIT
# Çelësi për randomizimin e pikselave (duhet të jetë i njëjtë në extract)
key = 12345

# Kanali i ngjyrës që do përdoret (0=Red, 1=Green, 2=Blue)
colourPlane = 0

# Biti specifik ku do fshihet informacioni (LSB ose bit i zgjedhur)
significantBit = 7

# Imazhi bazë (cover image)
coverImage = "img/flowers.bmp"

# File që përmban mesazhin sekret
secretFile = "secret.txt"

# Imazhi i output-it me mesazhin e fshehur
outputImage = "stego-img.bmp"


# 2. LEXIMI I TË DHËNAVE

# Hap imazhin dhe e konverton në RGB format
image = Image.open(coverImage).convert("RGB")

# Merr dimensionet e imazhit
dimensions = image.size

# Merr akses në pikselat e imazhit
pixels = image.load()

# Lexon mesazhin sekret nga file
with open(secretFile, "r", encoding="utf-8") as f:
    secret = f.read()

# 3. PËRGATITJA E MESAZHIT

# Numri total i pikselave në imazh
total_pixels = dimensions[0] * dimensions[1]

# Konvertimi i mesazhit në ASCII 7-bit
sbits = ''.join(format(ord(char), 'b').zfill(7) for char in secret)

# 14 bitët e parë përdoren për gjatësinë e mesazhit
lbits = format(len(secret), 'b').zfill(14)

# Bashkimi i gjatësisë + mesazhit
bits = lbits + sbits

# Kontrollon nëse imazhi ka kapacitet të mjaftueshëm
if len(bits) > total_pixels:
    raise ValueError("Image does not have enough capacity!")

# 4. RANDOMIZIMI I PIKSELAVe

# Krijon listë me indeksat e pikselave
shuffledIndices = list(range(total_pixels))

# Përzien indeksat në mënyrë të kontrolluar me key
random.seed(key)
random.shuffle(shuffledIndices)

# 5. FUNKSION NDËRHYRJE NË PIXEL

# Funksion që modifikon një pixel duke ndryshuar bitin e zgjedhur
def modify_pixel(pixel, plane, bit, modifier):
    m = modifier * (2 ** (7 - bit))

    # Apliko ndryshimin në kanalin e zgjedhur të ngjyrës
    r = pixel[0] + m if plane == 0 else pixel[0]
    g = pixel[1] + m if plane == 1 else pixel[1]
    b = pixel[2] + m if plane == 2 else pixel[2]

    # Siguron që vlerat mbesin në intervalin 0-255
    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))

    return (r, g, b)

# 6. FSHEHJA E MESAZHIT
for i in range(len(bits)):

    # Gjen koordinatat e pikselit
    x = shuffledIndices[i] % dimensions[0]
    y = shuffledIndices[i] // dimensions[0]

    # Merr pixelin aktual
    pixel = pixels[x, y]
    value = pixel[colourPlane]

    # Konverton vlerën e ngjyrës në binar (8-bit)
    p = format(value, 'b').zfill(8)

    # Nëse biti nuk përputhet me mesazhin, e ndryshon pixelin
    if p[significantBit] == '0' and bits[i] == '1':
        pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, 1)

    elif p[significantBit] == '1' and bits[i] == '0':
        pixels[x, y] = modify_pixel(pixel, colourPlane, significantBit, -1)

# 7. RUAJTJA E IMAZHIT FINAL
# Ruaj imazhin me mesazhin e fshehur
image.save(outputImage)

print("Embedding complete. Output saved as:", outputImage)
