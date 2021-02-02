/*
** EPITECH PROJECT, 2020
** my_compute_factorial_it.c
** File description:
** 'fctiterative"
*/

int my_compute_factorial_it(int nb)
{
    int a = 1;
    int result = nb;
    if (nb == 0) return (1);
    if (nb < 0 || nb >= 13) return (0);
    if (nb > 0)
    {
        while (a != nb)
        {
            result = result * (nb - a);
            a++;
        }
    }
    return (result);
}
