from math import floor, pi, sin, cos
from numpy import linspace


def correct_params(arc_length, depth, spacing_desired, vel):
    res = 100

    segments = round(arc_length / spacing_desired)  # return stroke is opposite direction if segments is even
    spacing = arc_length / segments
    path_length = (depth - spacing) * (segments+1) + spacing + pi * spacing/2 * segments
    n = round(path_length*res)
    t_end = path_length/vel

    return segments, t_end, spacing, n


def path(depth, spacing, vel, t_end, n, segments):

    dt = t_end / n
    t_rise = (depth - spacing) / vel
    t_adv = (spacing * pi) / (2 * vel)
    p_u = t_rise + t_adv

    t_pad = spacing / (2 * vel)
    n_pad = round(t_pad / dt)
    u = n_pad * [0]
    v = list(linspace(0, spacing/2, n_pad))

    for i in range(n_pad, n - n_pad):
        t = dt * i - t_pad
        period_number_u = floor(t / p_u)
        t_shift = t - period_number_u * p_u

        if t_shift < t_rise:
            u.append(period_number_u * spacing)
            if period_number_u % 2 == 0:
                v.append(vel * t_shift + spacing / 2)
            else:
                v.append(- vel * t_shift + depth - spacing / 2)

        else:
            p = (pi / t_adv) * (t_shift - t_rise) + 3 / 2 * pi
            u.append(spacing / 2 * sin(p) + period_number_u * spacing + spacing / 2)

            if period_number_u % 2 == 0:
                v.append(spacing / 2 * cos(p) + depth - spacing / 2)
            else:
                v.append(spacing / 2 * cos(p + pi) + spacing / 2)

    for i in range(n_pad):
        u.append(u[-1])

    if segments % 2 == 0:
        a = linspace(v[-1], v[-1] + spacing/2, n_pad)
        for i in range(n_pad):
            v.append(a[i])
    else:
        a = linspace(v[-1], 0, n_pad)
        for i in range(n_pad):
            v.append(a[i])

    return [u, v]
