# coding: utf-8 
# license: GPLv3

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.
    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!
        r = ((body.x - obj.x)**2 + (body.y - obj.y)**2)**0.5
        body.Fx += gravitational_constant*body.m*obj.m/r**3*(obj.x-body.x)   # FIXME: нужно вывести формулу...
        body.Fy += gravitational_constant*body.m*obj.m/r**3*(obj.y-body.y)  # FIXME: нужно вывести формулу...


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    scale = 1
    ax = body.Fx/body.m
    body.x += scale*(body.Vx*dt + scale*dt**2*ax/2)
    body.Vx += ax*dt
    ay = body.Fy/body.m
    body.y += scale*(body.Vy*dt + scale*dt**2*ay/2)
    body.Vy += ay*dt
    print(body.x, body.y)
    # TODO не работает (((


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.
    **dt** — шаг по времени
    """

    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
