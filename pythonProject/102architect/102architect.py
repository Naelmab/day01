#!/usr/bin/env python3
##
## EPITECH PROJECT, 2020
## 102archi
## File description:
## 102archi
##

import sys
import math

if len(sys.argv) != 8 or int(sys.argv[7]) < 0 or int(sys.argv[7]) != int(sys.argv[7]):
    sys.exit(84)

class coordonnees0():
        x = float(float(sys.argv[4]) - float(sys.argv[1]))
        y = float(float(sys.argv[5]) - float(sys.argv[2]))
        z = float(float(sys.argv[6]) - float(sys.argv[3]))


class coordonnees1():
    coordonnee0 = coordonnees0()
    x1 = float(float(coordonnee0.x) * int(sys.argv[7]) + float(sys.argv[4]))
    y1 = float(float(coordonnee0.y) * int(sys.argv[7]) + float(sys.argv[5]))
    z1 = float(float(coordonnee0.z) * int(sys.argv[7]) + float(sys.argv[6]))


class coordonnees2():
    coordonnee1 = coordonnees1()
    x2 = float(coordonnee1.x1 - float(sys.argv[1]))
    y2 = float(coordonnee1.y1 - float(sys.argv[2]))
    z2 = float(coordonnee1.z1 - float(sys.argv[3]))


class temps0():
    n = int(int(sys.argv[7]))


class incidence_angle():
    coordonnee2 = coordonnees2()
    lenght_u = float(math.sqrt(pow(coordonnee2.z2, 2)))
    lenght_v = float(math.sqrt(pow(coordonnee2.x2, 2) + pow(coordonnee2.y2, 2) + pow(coordonnee2.z2, 2)))
    mul_lenght = float(lenght_u * lenght_v)
    result = float(pow(coordonnee2.z2, 2) / mul_lenght)
    final_result = 90 - float(math.acos(result)) * 180 / math.pi


def main():
    if len(sys.argv) == 8:
        print("The velocity vector of the ball is:")
        coordonnee0 = coordonnees0()
        print("({0:.2f}, {1:.2f}, {2:.2f})".format(coordonnee0.x, coordonnee0.y, coordonnee0.z))
        temps1 = temps0()
        print("At time t + {}, ball coordinates will be:".format(temps1.n))
        coordonnee1 = coordonnees1()
        print("({0:.2f}, {1:.2f}, {2:.2f})".format(coordonnee1.x1, coordonnee1.y1, coordonnee1.z1))
    if 0 > float(sys.argv[6]) > float(sys.argv[3]) and coordonnee1.z1 > 0 or 0 < float(sys.argv[6]) < float(sys.argv[3]) and coordonnee1.z1 < 0:
        print("The incidence angle is:")
        incidence_angle0 = incidence_angle()
        print("{:.2f} degrees".format(incidence_angle0.final_result))
    elif coordonnee0.z == 0 and coordonnee0.x == 0 and coordonnee0.y != 0 or coordonnee0.z == 0 and coordonnee0.x != 0 and coordonnee0.y == 0:
        print("The incidence angle is:\n0.00 degrees")
    else:
        print("The ball won't reach the paddle.")


if __name__ == '__main__':
    main()