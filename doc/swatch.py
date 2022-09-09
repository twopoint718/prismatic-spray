import math
import png

def hToRGB(H, S=1, L=0.5):
    C = 1
    X = 1 - math.fabs((H / 60.0) % 2 - 1)
    m = L - C/2.0
    r = 0
    g = 0
    b = 0
    if H >= 0 and H < 60:
        r, g, b = (C, X, 0)
    elif H >= 60 and H < 120:
        r, g, b = (X, C, 0)
    elif H >= 120 and H < 180:
        r, g, b = (0, C, X)
    elif H >= 180 and H < 240:
        r, g, b = (0, X, C)
    elif H >= 240 and H < 300:
        r, g, b = (X, 0, C)
    else:
        r, g, b = (C, 0, X)
    return (int(r * 255), int(g * 255), int(b * 255))

n = 50
row = []
for h in range(0, 360, 15):
    r, g, b = hToRGB(h)
    row.extend([r, g, b] * n)

rows = [row for _ in range(n)]

f = open('swatch.png', 'wb')
w = png.Writer(24 * n, n, greyscale=False)
w.write(f, rows)
f.close()