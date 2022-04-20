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
    dark = [int(x[0]) for x in f_result if 'B' in x]
    light = [int(x[0]) for x in f_result if 'L' in x]

    print('Results of force dice: ')
    if sum(dark) > 0:
        print(f'{sum(dark)} dark side.')
    if sum(light) > 0:
        print(f'{sum(light)} light side.')

    return f_result

#translate net results
def results_text(good_v, good_n, good_h, bad_v, bad_n, bad_h):
    #compute results
    vant = sum(good_v) - sum(bad_v)
    norm = sum(good_n) - sum(bad_n)
    hype = sum(good_h) - sum(bad_h)

    #print results
    res_strings = []
    print('Net results of Roll: ')
    if (vant == 0) and (norm == 0) and (hype == 0):
        print('It was a wash! Net zero!')
    else:
        if vant < 0:
            res_strings.append(f'{abs(vant)} disadvantage')
        elif vant > 0:
            res_strings.append(f'{abs(vant)} advantage')
        if norm < 0:
            res_strings.append(f'{abs(norm)} failure')
        elif norm > 0:
            res_strings.append(f'{abs(norm)} success')
        if hype < 0:
            res_strings.append(f'{abs(hype)} DISPAIR')
        elif hype > 0:
            res_strings.append(f'{abs(hype)} TRIUMPH')
    print(*res_strings, sep = ', ')
    return vant, norm, hype

#print roll results, not the net results
def roll_text(list):
    res_strings = []
    #good results
    good_v = [int(x[0]) for x in list if 'A' in x]
    good_n = [int(x[0]) for x in list if 'S' in x]
    good_h = [1 for x in list if 'GH' in x]

    #bad results
    bad_v = [int(x[0]) for x in list if 'D' in x]
    bad_n = [int(x[0]) for x in list if 'F' in x]
    bad_h = [1 for x in list if 'BH' in x]


    if (sum(good_v) != 0):
        res_strings.append(f'{sum(good_v)} advantage')
    if (sum(good_n) != 0):
        res_strings.append(f'{sum(good_n)} success')
    if (sum(good_h) != 0):
        res_strings.append(f'{sum(good_h)} TRIUMPH')
    if (sum(bad_v) != 0):
        res_strings.append(f'{sum(bad_v)} disadvantage')
    if (sum(bad_n) != 0):
        res_strings.append(f'{sum(bad_n)} failure')
    if (sum(bad_h) != 0):
        res_strings.append(f'{sum(bad_h)} DISPAIR')

    print('Results of Roll: ')
    print(*res_strings, sep = ', ')
    return good_v, good_n, good_h, bad_v, bad_n, bad_h

#initiative roller
def init_roll(char, rk = 0):
    if rk == 0:
        res = roll(green, char)
        roll_text(res)
        return res
    elif (char == rk) & (rk != 0):
        res = roll(yellow, char)
        roll_text(res)
        return res
    else:
        upped = min(char, rk)
        nor = max(char, rk) - upped
        res = roll(yellow, upped) + roll(green, nor)
        roll_text(res)
        return res

#skill rollers
def sk_roll(bv, gn, yh, bbv, pn, rh):
    main_res = roll(blue, bv) + roll(green, gn) + roll(yellow, yh) + roll(black, bbv) + roll(purple, pn) + roll(red, rh)
    good_v, good_n, good_h, bad_v, bad_n, bad_h = roll_text(main_res)
    results_text(good_v, good_n, good_h, bad_v, bad_n, bad_h)
    return main_res
