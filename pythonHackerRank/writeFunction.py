"""
In the Gregorian calendar, three conditions are used to identify leap years:

    The year can be evenly divided by 4, is a leap year, unless:
        The year can be evenly divided by 100, it is NOT a leap year, unless:
            The year is also evenly divisible by 400. Then it is a leap year.
"""
'''
Se houver resto na divisao por 4 entao e ano bissexto.

'''


def ano_bissexto(ano):
    if ano % 4 == 0:
        print('E ano bissexto')
    else:
        print('nao é ano bissexto')


ano = int(input())

ano_bissexto(ano)
