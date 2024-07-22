import math
import os
import vec as v


# нахождение пересечения сферы радиуса r c цетром в точке (0, 0)
# и вектора с началом ro и направлением rd
def sphere(ro: v.vec3, rd: v.vec3, r: int) -> v.vec2:
    b = v.vec3.dot(rd, ro)
    c = v.vec3.dot(ro, ro) - r * r
    d = b * b - c
    if d < 0:
        return v.vec2(-1, -1)
    return v.vec2(-b - d**0.5, -b + d**0.5)


def clump(value: float, max_v: int, min_v: int) -> float:
    return max(min(value, max_v), min_v)


width, height = os.get_terminal_size()
aspect = width / height
pixel_aspect = 11 / 24
gradient = " .:!/r(l1Z4H9W8$@"
dtx = 0.01
dty = 0.01

donut = [" " for _ in range(width * height + 1)]
donut[width * height] = "\n"

for t in range(20000):
    light = v.vec3(
        math.sin(t * 0.01), math.cos(t * 0.01), -1
    ).norm()  # направление света
    for i in range(width):
        for j in range(height):
            uv = v.vec2(i, j) / v.vec2(width, height) * v.vec2(2, 2) - v.vec2(1, 1)
            uv.x *= aspect * pixel_aspect
            # uv.x += math.sin(t*0.01)

            ro = v.vec3(-2, 0, 0)
            rd = v.vec3(1, uv.x, uv.y).norm()

            color = 0
            intersection = sphere(ro, rd, 1)

            if intersection.x > 0:
                itPoint = ro + rd * v.vec3(
                    intersection.x, intersection.x, intersection.x
                )
                n = itPoint.norm()
                diff = v.vec3.dot(
                    n, light
                )  # насколько сильно света повёрнута к источнику света
                color = int(diff * 20)
            color = clump(color, len(gradient) - 1, 0)
            pixel = gradient[int(color)]
            donut[i + width * j] = pixel
    print(*donut, sep="")
