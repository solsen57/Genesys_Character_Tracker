#file to view and update character sheet text file
import glob
import os

#list sheets and choose which to use
print('Here is a list of character sheets within this program: ')
#figure out how to deal with file path
os.chdir(r'C:\Users\sophi\github\Genesys_Character_Tracker')
chars_list = glob.glob('*.txt')
print(chars_list)
#make a dict of characters? have user select from list rather than type?
char_choice = input('Which character would you like to work with? ').lower()

#actions to character sheet
csh_check = input('Would you like to view or update your character sheet? ').lower()

if csh_check == 'view':
    pass
elif csh_check == 'update':
    pass
else:
    exit()
