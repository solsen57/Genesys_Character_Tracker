#file to maintain character sheet
import test_sheet2 as cc

#define skill types
br_skills = ["athletics", "resilience", "brawl", "melee"]
ag_skills = ["coordination", "piloting - planetary", "piloting - space", "stealth", "gunnery", "ranged - light", "ranged - heavy"]
int_skills = ["astrogation", "computers", "mechanics", "medicine", "core worlds", "education", "lore", "outer rim", "underworld", "warfare", "xenology"]
cun_skills = ["deception", "perception", "skulduggery", "streetwise", "survival"]
will_skills = ["coercion", "discipline", "vigilance"]
pr_skills = ["charm","cool", "leadership", "negotiation"]

csh_check = input('Would you like to view or update your character sheet? ').lower()

#print everthing
if csh_check == 'view':
    print('')
    print('Name: {}'.format(cc.char_name))
    print('--')
    print('Base Characteristics Stats: ')
    for key, val in cc.characteristics.items():
        new_key = key.capitalize()
        print('{} {}'.format(new_key, val))
    print('--')
    #append base characteristics to skill - clean up later
    print('Skill Stats: ')
    for key, val in cc.skills.items():
        if key in br_skills:
            new_key = key.capitalize()
            print('(BR) {} {}'.format(new_key, val))
        elif key in ag_skills:
            new_key = key.capitalize()
            print('(AG) {} {}'.format(new_key, val))
        elif key in int_skills:
            new_key = key.capitalize()
            print('(INT) {} {}'.format(new_key, val))
        elif key in cun_skills:
            new_key = key.capitalize()
            print('(CUN) {} {}'.format(new_key, val))
        elif key in will_skills:
            new_key = key.capitalize()
            print('(WIL) {} {}'.format(new_key, val))
        elif key in pr_skills:
            new_key = key.capitalize()
            print('(PR) {} {}'.format(new_key, val))
        else:
            new_key = key.capitalize()
            print('{} {}'.format(new_key, val))
