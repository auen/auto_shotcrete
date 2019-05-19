from math import sqrt
from numpy import linspace
from scipy import optimize
from scipy.linalg import norm


def fit(p, *n):
    if n == ():
        n = 1000
    n_reparam = 1000
    x_data = []
    y_data = []
    z_data = []
    d = []
    y_reparam = []
    z_reparam = []
    u_reparam = []
    u_coeffs = []
    u_scaled = linspace(0, 1, n_reparam)
    ut = linspace(0, 1, n)
    chord = []
    du = ut[1] - ut[0]
    parameter = []

    for i in range(len(p)):
        pt = p[i]
        x_data.append(pt[0])
        y_data.append(pt[1])
        z_data.append(pt[2])

    for i in range(1, len(p)):
        chord.append(sqrt((z_data[i]-z_data[i-1])**2+(y_data[i]-y_data[i-1])**2))

    chord_arc = sum(chord)

    for i in range(len(chord)):
        parameter.append(sum(chord[:i])/chord_arc)
    parameter.append(1)

    y_coeffs, y_cov = optimize.curve_fit(y_func, parameter, y_data)
    z_coeffs, z_cov = optimize.curve_fit(z_func, parameter, z_data)

    for i in range(n):
        par = ut[i]

        yen = y_func(par + du, *y_coeffs)
        ye = y_func(par, *y_coeffs)
        zen = z_func(par + du, *z_coeffs)
        ze = z_func(par, *z_coeffs)

        d.append(sqrt((yen-ye)**2+(zen-ze)**2))
    perimeter = sum(d)

    if y_data[0] < y_data[-1]:
        direction = 1
    else:
        direction = -1

    for i in range(n_reparam):
        y_reparam.append(y_func(u_scaled[i], *y_coeffs))
        z_reparam.append(z_func(u_scaled[i], *z_coeffs))

    for i in range(1, n_reparam):
        u_reparam.append(sqrt((z_reparam[i]-z_reparam[i-1])**2+(y_reparam[i]-y_reparam[i-1])**2))

    u_chord_arc = sum(u_reparam)

    for i in range(len(u_reparam)):
        u_coeffs.append(sum(u_reparam[:i]))
    u_coeffs.append(u_chord_arc)

    u_coeffs, u_cov = optimize.curve_fit(u_func, u_coeffs, u_scaled)

    return perimeter, x_data[0], [y_coeffs, z_coeffs, u_coeffs, direction]


def y_func(x, a, b, c, d):
    return a * x**3 + b * x**2 + c * x + d


def y_func_diff(x, a, b, c, d):
    return 3 * a * x**2 + 2 * b * x + c


def z_func(x, a, b, c, d, e):
    return a * x**4 + b * x**3 + c * x**2 + d * x + e


def z_func_diff(x, a, b, c, d, e):
    return 4 * a * x**3 + 3 * b * x**2 + 2 * c * x + d


def u_func(x, a, b, c, d, e, f):
    return a * x**5 + b * x**4 + c * x**3 + d * x**2 + e * x + f


def surf(uv_list, params, offset):
    u = uv_list[0]
    v = uv_list[1]
    y_coeffs = params[0]
    z_coeffs = params[1]
    u_coeffs = params[2]
    direction = params[3]
    x = []
    y = []
    z = []
    nx = []
    ny = []
    nz = []

    for i in range(len(u)):
        par = u_func(u[i], *u_coeffs)
        x.append(v[i] + offset)
        y.append(y_func(par, *y_coeffs))
        z.append(z_func(par, *z_coeffs))

        x_diff = 0
        y_diff = y_func_diff(par, *y_coeffs)
        z_diff = z_func_diff(par, *z_coeffs)

        scale = -direction*norm([x_diff, y_diff, z_diff])

        nx.append(0)
        ny.append(z_diff/scale)
        nz.append(-y_diff/scale)

    return [x, y, z, nx, ny, nz]
