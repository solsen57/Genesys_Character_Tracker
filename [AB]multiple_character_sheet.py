#file to view and update character sheet text file
import glob
import os

#list sheets and choose which to use
print('Here is a list of character sheets within this program: ')
#figure out how to deal with file path - automate it or something
path = 'C:\\Users\sophi\github\Genesys_Character_Tracker\Sheets'
chars_list_init = os.listdir(path)
chars_list = [os.path.splitext(x)[0] for x in chars_list_init]
chars_dict = dict(enumerate(chars_list, start = 1))
for key, val in chars_dict.items():
    print('[{}] {}'.format(key, val))

#make a dict of characters? (y) have user select from list rather than type? (y)
char_choice = int(input('Which character would you like to work with? '))
def checkChar(choice):
    for key in chars_dict:
        if choice == key:
            wrk_char = chars_dict[key]
            wrk_char_imp = wrk_char + '.py'
            print(wrk_char)
            import wrk_char_imp as wc
            return wrk_char
        else:
            print('invalid')
            exit()
cur_char = checkChar(char_choice)

#actions to character sheet
csh_check = input('Would you like to view or update your character sheet? ').lower()

if csh_check == 'view':
    print('Viewing character sheet for {}'.format(cur_char))
elif csh_check == 'update':
    print('Updating character sheet for {}'.format(cur_char))
else:
    exit()
