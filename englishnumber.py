#Works till the 9th digit


def englishnumber(number):
    """facilitates to call number names to make anothers number names"""
    if number == 0:
        return 'zero'
    else:
        number = remove_0(str(number))
        if len(str(number)) <= 2:
            return two_numbers(number)

        if len(str(number)) == 3:
            return three_numbers(number)

        if len(str(number)) == 4:
            return four_numbers(number)

        if len(str(number)) == 5:
            return five_numbers(number)

        if len(str(number)) == 6:
            return six_numbers(number)

        if len(str(number)) in [7,8,9]:
            return seveneightnine_numbers(number)


def remove_0(number):
    """return a string whithout the left-sided zeros in a string-format number"""
    while number[0] == "0":
        number = number[1:]
    return number


def sum_base_10(number):
    """return a list with the terms of its base 10 decomposition"""
    string = str(number)
    numeros = []
    for num in range(len(string)-1, -1, -1):
        numeros.append(int(string[len(string)-1-num])*10**num)
    return numeros


def two_numbers(x):
    """return the name of a 2-digit number"""
    number = remove_0(str(x))
    if str(number) in MainNumbers.keys():
        return MainNumbers[str(number)]
    else:
        aux = sum_base_10(number)
        return f'{MainNumbers[str(aux[0])]}-{MainNumbers[str(aux[1])]}'


def three_numbers(number):
    """return the name of a 3-digit number"""
    if str(number)[-2:] == '00':
        return f'{MainNumbers[str(number)[0]]} hundred'
    else:
        number = remove_0(str(number))
        return f'{MainNumbers[str(number)[0]]} hundred and {two_numbers(remove_0(str(number)[1:]))}'


def four_numbers(number):
    """return the name of a 4-digit number"""
    if str(number)[-3:] == '000':
        return f'{MainNumbers[str(number)[0]]} thousand'
    else:
        return f'{MainNumbers[str(number)[0]]} thousand and {englishnumber(str(number)[1:])}'


def five_numbers(number):
    """return the name of a 5-digit number"""
    if str(number)[-3:] == '000':
        return f'{englishnumber(str(number)[0:2])} thousand'
    else:
        return f'{englishnumber(str(number)[0:2])} thousand and {englishnumber(str(number)[2:])}'

      
def six_numbers(number):
    if str(number)[-3:] == '000':
        return f'{englishnumber(str(number)[0:3])} thousand'
    else:
        return f'{englishnumber(str(number)[0:3])} thousand and {englishnumber(str(number)[3:])}'


def seveneightnine_numbers(number):
    if str(number)[-6:] == '000000':
        return f'{englishnumber(str(number)[:-6])} million'
    else:
        return f'{englishnumber(str(number)[:-6])} million, {englishnumber(str(number)[-6:])}'


MainNumbers = {'0':'zero',
               '1':'one',
               '2':'two',
               '3':'three',
               '4':'four',
               '5':'five',
               '6':'six',
               '7':'seven',
               '8':'eight',
               '9':'nine',
               '10':'ten',
               '11':'eleven',
               '12':'twelve',
               '13':'thirteen',
               '14':'fourteen',    
               '15':'fifteen',
               '16':'sixteen',
               '17':'seventeen',
               '18':'eighteen',
               '19':'nineteen',
               '20':'twenty',
               '30':'thirty',
               '40':'forty',
               '50':'fifty',
               '60':'sixty',
               '70':'seventy',
               '80':'eighty',
               '90':'ninety',
               '100':'hundred',
               '1000':'thousand'}


while True:
    x = int(input('\n\nDeseja saber o nome de que número? [0] para encerrar\n'))
    if x == 0:
        break
    else:
        print(englishnumber(x).capitalize())
print('Programa finalizado =)')
