/*
** EPITECH PROJECT, 2020
** tools
** File description:
** tools
*/

#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>

#include "my.h"

void my_putchar(char c)
{
    write(1, &c, 1);
}

int my_put_nbr(int nb)
{
    int ret = 0;

    if (nb < -2147483647)
        return (0);
    if (nb < 0)
    {
        my_putchar ('-');
        nb = nb * -1;
    }
    if (nb >= 0)
    {
        if (nb > 9)
        {
            ret = (nb % 10);
            nb = nb / 10;
            my_put_nbr(nb);
            my_put_nbr(ret);
        } else
            my_putchar(48 + nb);
    }
    return (0);
}

int ALLFACT(char **str) {
    int op3 = brakets(str);
    int op3bis = op3;

    MODULO(str, &op3bis);
    DIVIS(str, &op3bis);
    MULTI(str, &op3bis);

    return (op3bis);
}

int chartoint(char **str)
{
    int number = 0;

    while (**str >= '0' && **str <= '9') {
        number = number * 10 + (**str - '0');
        (*str)++;
    }
    return (number);
}

int brakets(char **str)
{
    if (**str == '(') {
        ++(*str);
        int res = ADD(str) + SUB(str);
        ++(*str);
        return (res);
    }
    return (chartoint(str));
}