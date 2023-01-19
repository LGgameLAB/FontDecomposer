from fontTools.ttLib import TTFont
from pygame import Vector2 as Vec
font1 = TTFont('PerfectDOSVGA437.ttf')
# for key, value in font.reader.tables.items():
#     print(key, value)
# print(font1["glyf"]["f"].__dict__)
# print(vars(font.reader.tables["glyf"]))

def transform(l, scale, shift):
    l2 = []
    for v in l:
        new = Vec(v)*scale + shift
        l2.append((new.x, new. y))

    return l2

def getPolysFromString(font, phrase):
    polys = []
    x2 = 0
    for c in [*phrase]:
        charData = font["glyf"][c]
        for x in range(charData.numberOfContours):
            start = 0 if x == 0 else charData.endPtsOfContours[x-1]+1
            end = charData.endPtsOfContours[x]
            polys.append(transform(charData.coordinates[start:end+1], 1/256, (7*x2, 0)))
        x2 += 1
    
    return polys

for x in [f"polygon({str(v)})" for v in getPolysFromString(font1, "Ellis")]:
    print(x + ", ", end="") 