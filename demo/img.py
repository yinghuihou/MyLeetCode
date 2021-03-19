from PIL import Image

img = Image.open("yb_ic_bank_card.png")
img = img.convert('RGBA')
x, y = img.size

for i in range(x):
    for j in range(y):
        try:
            r, g, b, alpha = img.getpixel((i, j))
            print("r: " + str(r) + "  g: " + str(g) + "  b: " + str(b))
            if r == g and g == b:
                continue
            else:
                img.putpixel((i, j), (148, 0, 211, alpha))
        except Exception as e:
            print(e)
            continue

img.save("ss.png")
img.show()
