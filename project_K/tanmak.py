import math


def init_circle_bullets(n, speed, odd):
    vx = []
    vy = []
    rad_step = (math.pi * 1.0) / n
    rad = 0

    if(odd):
    #when odd
        rad = rad_step / 2.0

    for i in range(n):
        vx.append(math.cos(rad) * speed)
        vy.append(math.sin(rad) * speed)
        rad = rad + rad_step

    return (vx, vy)


def rotate_velocity(theta, vx0, vy0):
    rad = (math.pi / 180.0) * theta
    c = math.cos(rad)
    s = math.sin(rad)
    vx = vx0 * c - vy0 * s
    vy = vx0 * s + vy0 * c

    return (vx, vy)


def rotate_velocity_rad(rad, vx0, vy0):
    c = math.cos(rad)
    s = math.sin(rad)
    vx = vx0 * c - vy0 * s
    vy = vx0 * s + vy0 * c

    return (vx, vy)


def init_nway_bullets(vx0, vy0, theta, n):
    vx = []
    vy = []
    rad_step = (math.pi / 180.0) * theta
    det = n % 2
    rad = (-n / 2.0 + 0.5) * rad_step #rad = (-n / 2.0 + 0.5) * rad_step
    if(det == 1):
        rad = (-n / 2.0) * rad_step #rad = (-n / 2.0) * rad_step


    for i in range(n):
        c = math.cos(rad)
        s = math.sin(rad)
        vx.append(vx0 * c - vy0 * s)
        vy.append(vx0 * s + vy0 * c)
        rad = rad + rad_step

    return (vx, vy)

	
def update_guided_bullets(bullet_x, bullet_y, vx, vy, hero_x, hero_y):
# bullet_x = current x-axis position
# bullet_y = current y-axis position
# vx = current x-axis speed
# vy = current y-axis speed
# hero_x, hero_y = current hero x  and y position

    vec_x = (hero_x - bullet_x)
    vec_y = (hero_y - bullet_y)
    norm = math.sqrt(vec_x * vec_x + vec_y * vec_y)
    vec_x = vec_x / norm
    vec_y = vec_y / norm
    alpha = math.sqrt(math.pow(vx, 2) + math.pow(vy, 2))

    return (-alpha * vec_x, -(alpha*vec_y))  # returns changed vx, vy
