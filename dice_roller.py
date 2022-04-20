#define dice and set up fucntions for rollers (force, skill, initiative?)

import random

#define dice outcomes
blue = ['Blank', 'Blank', '1S', '1S, 1A', '2A', '1A']
green = ['Blank', '1S', '1S', '2S', '1A', '1A', '1S, 1A', '2A']
yellow = ['Blank', '1S', '1S', '2S', '2S', '1A', '1S, 1A', '1S, 1A', '1S, 1A', '2A', '2A', 'GH']
black = ['Blank', 'Blank', '1F', '1F', '1D', '1D']
purple = ['Blank', '1F', '1D', '2F', '1D', '1D', '1F, 1D', '2D']
red = ['Blank', '1F', '1F', '2F', '2F', '1D', '1D', '1F, 1D', '1F, 1D', '2D', '2D', 'BH']
white = ['1B', '1B', '1B', '1B', '1B', '1B', '2B', '1L', '1L', '2L', '2L', '2L']

#basic roll function
def roll(color, number):
    i = 1
    result = []
    while i <= number:
        result.append(random.choice(color))
        i += 1
    return result

#force dice roller
def force_roll(fw = 1):
    f_result = roll(white, fw)

    #separate light side and dark side
    dark = [x for x in f_result if 'B' in x]
    c_dark = [int(x[0]) for x in dark]
    light = [x for x in f_result if 'L' in x]
    c_light = [int(x[0]) for x in light]

    print('Results of force dice: ')
    if sum(c_dark) > 0:
        print(f'{sum(c_dark)} dark side.')
    if sum(c_light) > 0:
        print(f'{sum(c_light)} light side.')

    return f_result

#translate results
def results_text(list):
    pass

#initiative roller
def init_roll(cha = 1, rk = 0):
    if rk == 0:
        res = roll(green, cha)
        print('1')
        print(res)
        return res
    elif (cha == rk) & (rk != 0):
        res = roll(yellow, cha)
        print('2')
        print(res)
        return res
    else:
        upped = min(cha, rk)
        nor = max(cha, rk) - upped
        res = roll(yellow, upped) + roll(green, nor)
        print('3')
        print(upped)
        print(nor)
        print(res)
        return res

init_roll(4, 1)
