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
