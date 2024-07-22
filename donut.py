import vec as v
import math
import os


def clump(value: int, max_v: int, min_v: int) -> int:
    return max(min(value, max_v), min_v)


def get_dist_donut(p: v.vec3, t=v.vec2(1.0, 0.5)) -> float:
    return v.vec2(v.vec2(p.x, p.y).length() - t.x, p.z).length() - t.y


def rotate(tx: float | None, ty: float | None, p: v.vec3) -> v.vec3:
    if tx is not None:
        p = v.vec3(
            p.x,
            p.y * math.cos(tx) + p.z * math.sin(tx),
            -p.y * math.sin(tx) + p.z * math.cos(tx),
        )

    if ty is not None:
        p = v.vec3(
            p.x * math.cos(ty) - p.z * math.sin(ty),
            p.y,
            p.x * math.sin(ty) + p.z * math.cos(ty),
        )

    return p


def march(ro: v.vec3, rd: v.vec3, tx: float | None = None) -> float:
    dist = 1
    p = ro + rd
    delta = get_dist_donut(p)
    dist += delta
    p_next = p + rd * delta
    while (p - p_next).length() > 0.0005 and dist < 100:
        p, p_next = p_next, p
        delta = get_dist_donut(p)
        dist += delta
        p_next = p + rd * delta

    return dist


width, height = os.get_terminal_size()
aspect = width / height
pixel_aspect = 11 / 24
gradient = ".:!/r(l1Z4H9W8$@"
dtx = 0.01
dty = 0.01

donut = [" " for _ in range(width * height + 1)]
donut[width * height] = "\n"

for t in range(20000):
    for i in range(width):
        for j in range(height):
            uv = v.vec2(i, j) / v.vec2(width, height) * 2.0 - 1.0
            uv.x *= aspect * pixel_aspect
            # additional movement on the console
            # uv.x += math.sin(t*0.02)
            # uv.y += math.sin(t*0.01)

            ro = v.vec3(-2.5, 0, 0)
            ro = rotate((t * 0.02) * math.pi, (t * 0.03) * math.pi, ro)
            rd = v.vec3(1, uv.x, uv.y).norm()
            rd = rotate((t * 0.02) * math.pi, (t * 0.03) * math.pi, rd)

            distance = march(ro, rd)
            if distance < 100:
                color = int(math.exp(distance))
                color = clump(color, len(gradient) - 1, 0)
                pixel = gradient[-1 - color]
            else:
                color = 0
                pixel = " "
            donut[i + width * j] = pixel
    print("\x1b[H", end="")
    print(*donut, sep="")
