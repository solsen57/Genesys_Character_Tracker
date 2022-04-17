#file to create text doc for character sheet

cs_ver = input('Would you like to create a new character (y/n)? ').lower()

#add error, yes/no lists, find way to exit back to main menu
if cs_ver.startswith('y'):
    print('yes')
else:
    exit()

#create text file; text name is character name - lowercase
