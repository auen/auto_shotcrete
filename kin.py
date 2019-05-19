from copy import deepcopy
from numpy import sin, cos, pi, tan, arctan, array, arctan2, square, arcsin, savetxt
from math import pi, inf, sqrt, radians


def fk(q):
    # Geometry
    a1 = 0.235
    a2 = 0.355
    a4 = 0.20098
    a5 = 0.345
    d1 = 0.505
    d5 = 0.00837
    d6 = 0.6928

    # DH table
    dh = array([[q[0], d1, -a1, pi / 2],
                [(q[1] + pi / 2), 0, a2, pi / 2],
                [0, q[2], 0, 0],
                [q[3], 0, -a4, pi / 2],
                [q[4], -d5, -a5, -pi / 2],
                [0, d6, 0, 0]])

    # Transformation matrices
    t1 = t_dh(dh[0, :])
    t2 = t_dh(dh[1, :])
    t3 = t_dh(dh[2, :])
    t4 = t_dh(dh[3, :])
    t5 = t_dh(dh[4, :])
    t6 = t_dh(dh[5, :])

    t = t1 @ t2 @ t3 @ t4 @ t5 @ t6

    return t


def t_dh(u):
    a = rot_z(u[0])
    b = trans_z(u[1])
    c = trans_x(u[2])
    d = rot_x(u[3])

    t = a @ b @ c @ d

    return t


def rot_z(theta):
    u = array([[cos(theta), -sin(theta), 0, 0],
               [sin(theta),  cos(theta), 0, 0],
               [0,                    0, 1, 0],
               [0,                    0, 0, 1]])

    return u


def rot_x(alpha):
    u = array([[1,          0,           0, 0],
               [0, cos(alpha), -sin(alpha), 0],
               [0, sin(alpha),  cos(alpha), 0],
               [0,          0,           0, 1]])

    return u


def trans_x(a_n):
    u = array([[1, 0, 0, a_n],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]])

    return u


def trans_z(d_n):
    u = array([[1, 0, 0,    0],
               [0, 1, 0,    0],
               [0, 0, 1,  d_n],
               [0, 0, 0,    1]])

    return u


def fk_wrist(q):
    # Geometry
    a4 = 0.20098
    a5 = 0.345
    d5 = 0.00837
    d6 = 0.6928

    # DH table
    dh = array([[q[0],       0, -a4,  pi/2],
               [q[1],      -d5, -a5, -pi/2],
               [0,          d6,   0,     0]])

    # Transformation matrices
    t1 = t_dh(dh[0, :])
    t2 = t_dh(dh[1, :])
    t3 = t_dh(dh[2, :])

    t = t1 @ t2 @ t3

    return t


def fk_boom(q):
    #  Geometry
    a1 = 0.235
    a2 = 0.355
    d1 = 0.505

    #  DH table
    dh = array([[q[0],               d1,  -a1, pi / 2],
                [(q[1] + pi / 2),     0,   a2, pi / 2],
                [0,                q[2],    0,      0]])

    # Transformation matrices
    t1 = t_dh(dh[0, :])
    t2 = t_dh(dh[1, :])
    t3 = t_dh(dh[2, :])
    t = t1 @ t2 @ t3

    return t


def ik_wrist(qb, rx, ry):
    t2 = tan(ry / 2)
    t3 = t2 ** 2
    t5 = tan(qb[0] / 2)
    t6 = t5 ** 2
    t7 = t3 * t6
    t11 = tan(qb[1] / 2 + pi / 4)
    t14 = tan(rx / 2)
    t15 = t14 * t5
    t16 = t11 ** 2
    t19 = t14 ** 2
    t20 = t19 * t6
    t21 = t19 * t3
    t24 = t2 * t11
    t25 = 2 * t24
    t28 = 4 * t15 * t11
    t31 = t19 * t2
    t33 = 2 * t31 * t11
    t34 = t2 * t6
    t36 = 2 * t34 * t11
    t37 = t6 * t11
    t39 = 2 * t31 * t37
    t40 = t14 * t3
    t41 = t5 * t11
    t43 = 4 * t40 * t41
    t44 = t19 * t16 + t20 * t16 + t3 * t16 + t7 * t16 + t21 * t6 + t21 - t25 + t28 - t33 + t36 + t39 - t43 + t6 + 1
    t45 = t6 * t16
    t48 = t21 * t16 + t21 * t45 + t16 + t19 + t20 + t25 - t28 + t3 + t33 - t36 - t39 + t43 + t45 + t7
    t51 = sqrt(t44 / t48)
    t55 = t45 * t51
    t65 = t16 * t51
    t67 = t19 * t11 + t20 * t11 - t21 * t11 + t7 * t11 - 2 * t15 * t16 + t31 * t16 - t34 * t16 + t20 * t51 + 2 * t24 * t51 + t31 * t6 - 2 * t40 * t5 + t7 * t51 + 2 * t15 - t31 + t34 + t55 + t65
    t79 = t11 * t51
    t88 = t5 * t16
    t92 = -2 * t31 * t37 * t51 + 4 * t40 * t41 * t51 + t3 * t11 - 4 * t15 * t79 + t2 * t16 + t19 * t51 - t21 * t37 + t21 * t55 + t21 * t65 + t3 * t51 - t31 * t45 + 2 * t31 * t79 - 2 * t34 * t79 + 2 * t40 * t88 - t11 - t2 - t37
    t94 = t14 * t6
    t96 = t2 * t5
    t108 = t14 * t16 - t40 * t16 - t94 * t16 + 2 * t96 * t16 + 2 * t31 * t5 + 2 * t31 * t88 + t40 * t45 + t40 * t6 + t14 - t40 - t94 + 2 * t96
    t111 = arctan((t67 + t92) / t108)
    q_4 = 2 * t111

    t1 = sin(rx)
    t2 = cos(ry)
    t6 = qb[1] / 2 + pi / 4
    t7 = sin(t6)
    t8 = cos(t6)
    t10 = sin(qb[0])
    t13 = 2 * t1 * t2 * t7 * t8 * t10
    t14 = cos(rx)
    t15 = t14 * t2
    t16 = t8 ** 2
    t18 = 2 * t15 * t16
    t19 = sin(ry)
    t21 = cos(qb[0])
    t24 = 2 * t19 * t7 * t8 * t21
    t29 = sqrt(-(t13 + t18 - t24 - t15 + 1) / (t13 + t18 - t24 - t15 - 1))
    t30 = arctan(t29)
    q_5 = -2 * t30

    q = [q_4, q_5]

    return q


def ik_boom(x, y, z):

    q_1 = arctan2(y, x)
    q_2 = 2*arctan2((200*z*cos(q_1)-101*cos(q_1)+(7369*cos(q_1)**2-40400*z*cos(q_1)**2+40000*z**2*cos(
        q_1)**2+18800*x*cos(q_1)+40000*x**2)**(1/2)), (2*(100*x+59*cos(q_1))))-pi/2
    q_3 = -(71*cos(q_2)-200*z+101)/(200*sin(q_2))

    q = [q_1, q_2, q_3]

    return q


def ik_iter(cart_ref):
    tol = 1e-4
    max_iter = 10

    x = cart_ref[0]
    y = cart_ref[1]
    z = cart_ref[2]
    nx = cart_ref[3]
    ny = cart_ref[4]
    nz = cart_ref[5]
    counter = 0

    ry = arcsin(nx)
    rx = -arctan2(ny, nz)

    t = deepcopy([x, y, z])
    pos_err_magnitude = inf
    q = []

    while pos_err_magnitude > tol:

        q = ik_boom(t[0], t[1], t[2])
        q[3:] = ik_wrist(q[0:3], rx, ry)
        tf = fk(q)

        pos_err = array(tf[:3, 3] - [x, y, z])
        pos_err_magnitude = sqrt(sum(square(pos_err)))
        # print("Error after ", counter, " iterations: ", pos_err_magnitude)
        t = t - pos_err
        counter += 1
        if counter > max_iter:
            raise Exception('Failed to converge inverse kinematics after {} attempts'.format(max_iter))

    return q


def lim_check(q_ref):
    lim = array([[radians(-65), radians(65)],
                    [radians(-16), radians(57)],
                    [7.012, 15.012],
                    [-pi, pi],
                    [radians(-118), radians(62)]])

    for i in range(len(q_ref)):
        q = q_ref[i]

        if not lim[0, 0] <= q[0] <= lim[0, 1]:
            raise Exception("q1 out of range.")

        if not lim[1, 0] <= q[1] <= lim[1, 1]:
            raise Exception("q2 out of range.")

        if not lim[2, 0] <= q[2] <= lim[2, 1]:
            raise Exception("q3 out of range.")

        if not lim[3, 0] <= q[3] <= lim[3, 1]:
            raise Exception("q4 out of range.")

        if not lim[4, 0] <= q[4] <= lim[4, 1]:
            raise Exception("q5 out of range.")
